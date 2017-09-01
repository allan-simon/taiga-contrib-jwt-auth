Taiga contrib oauth2 jwt
=========================

Taiga plugin that use oauth2 with `authorization_code` code flow
and a JWT token decoded on the backend to get the user information

Installation
------------

### Taiga Back

In your Taiga back python virtualenv install the pip package `taiga-contrib-jwt-auth` with:

```bash
  pip install taiga-contrib-jwt-auth
```

Modify your settings/local.py and include the line:

```python
  INSTALLED_APPS += ["taiga_contrib_jwt_auth"]
```

### Taiga Front

Download in your `dist/plugins/` directory of Taiga front the `taiga-contrib-jwt-auth` compiled code:

```bash
  cd dist/plugins/
  svn export "https://github.com/allan-simon/taiga-contrib-jwt-auth/trunk/front/dist" "auth"

```
Download in your `dist/images/contrib` directory of Taiga front the `taiga-contrib-jwt-auth` sso icon:

```bash
  cd dist/images/contrib
  wget "https://raw.googleusercontent.com/taigaio/taiga-contrib-google-auth/stable/front/images/contrib/google-logo.png"
```

Include in your dist/conf.json in the contribPlugins list the value `"/plugins/auth/jwt_auth.json"`:

```json
    "contribPlugins": ["/plugins/auth/jwt_auth.json"]
```
