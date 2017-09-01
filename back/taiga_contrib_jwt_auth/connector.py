# Copyright (C) 2015 Allan Simon <allan.simon@supinfo.com>
# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from collections import namedtuple

import requests

import jwt

from django.conf import settings

from taiga.base.connectors.exceptions import ConnectorBaseException


######################################################
## Data
######################################################

User = namedtuple(
    "User",
    [
        "guid",
        "username",
        "email",
        "full_name",
    ],
)


######################################################
## Convined calls
######################################################

def get_user_info(code):

    response = requests.post(
        settings.OAUTH2_URL,
        data={
            'client_id': settings.OAUTH2_CLIENT_ID,
            'code': code,
            'grant_type': 'authorization_code',
            'redirect_uri': settings.OAUTH2_REDIRECT_URI,
        },
    )

    data = response.json()
    if response.status_code != 200:
        raise ConnectorBaseException(
            {
                "status_code": response.status_code,
                "error": data.get("error", "")
            },
        )

    token = data["access_token"]
    payload = jwt.decode(
        token,
        settings.JWT_PUBLIC_KEY,
        options={
            'verify_signature': True,
            'verify_exp': True,
            'required_exp': True,
        }
    )


    return User(
        guid=payload.get("userGUID", None),
        username=payload.get("email", None),
        full_name=payload.get("firstname", None) + " " + payload.get("lastname", None),
        email=payload.get("email", None),
    )
