(function() {
    'use strict';

    var module = angular.module('taigaContrib.pingfederateAuth', []);

    var PingFederateLoginButtonDirective = function(
        $window,
        $params,
        $location,
        $config,
        $events,
        $confirm,
        $auth,
        $navUrls,
        $loader
    ) {
        /**
         *
         */
        var link = function($scope, $el, $attrs) {

            var clientId = $config.get("", null);
            var loginOnSuccess = function(response) {
                var nextUrl = $navUrls.resolve("home");
                if (
                    $params.next &&
                    $params.next !== $navUrls.resolve("login")
                ) {
                    nextUrl = $params.next;
                }

                $events.setupConnection();
                $location.search("next", null);
                $location.search("code", null);

                var redirectToUri = $location.url(nextUrl).absUrl();
                return $window.location.href = redirectToUri;

            };

            var loginOnError = function(response) {
                $location.search("code", null);
                $loader.pageLoaded();
                if (response.data.error_message) {
                    return $confirm.notify(
                        "light-error",
                        response.data.error_message
                    );
                }
                return $confirm.notify(
                    "light-error",
                    "Our Oompa Loompas have not been able to get you credentials from Ping Federate."
                );
            };

            var loginWithPingFederateAccount = function() {
                var code = $params.code;
                if (!code) {
                    return;
                }
                $loader.start();
                var data = {
                    code: code
                };
                return $auth.
                    login(data, "pingfederate").
                    then(
                        loginOnSuccess,
                        loginOnError
                    )
                ;
            };

            loginWithPingFederateAccount();
            $el.on(
                "click",
                ".button-auth",
                function(event) {
                    var redirectToUri = $location.url($location.path()).absUrl();

                    var OAUTH2_URL = $config.get("OAuth2URL", null);
                    var REDIRECT_URL = $config.get("OAuth2RedirectURI", null);
                    var CLIENT_ID = $config.get("ClientID", null);
                    var url = "" + OAUTH2_URL +
                        "?redirect_uri=" + REDIRECT_URL +
                        "&client_id=" + CLIENT_ID +
                        "&response_type=code"
                    ;

                    return $window.location.href = url;
                }
            );

            return $scope.$on(
                "$destroy",
                function() { return $el.off(); }
            );
        };

        return {
            link: link,
            restrict: "EA",
            template: ""
        }
    };

    module.directive(
        "tgPingFederateLoginButton",
        [
            "$window",
            '$routeParams',
            "$tgLocation",
            "$tgConfig",
            "$tgEvents",
            "$tgConfirm",
            "$tgAuth",
            "$tgNavUrls",
            "tgLoader",
            PingFederateLoginButtonDirective
        ]
    );

    module.run([
        '$templateCache',
        function($templateCache) {
            return $templateCache.put(
                '/plugins/auth/ping_federate_auth.html',
                '<div tg-ping-federate-login-button="tg-ping-federate-login-button">' +
                    '<a href="" title="Enter with your SSO account" class="button button-auth">'+
                        '<img src="images/contrib/google-logo.png"/>' +
                        '<span>Login with SSO</span>' +
                    '</a>' +
                '</div>'
            );
        }
    ]);

}).call(this);
