(function () {

    var Pray = angular.module('prayerApp',
        ['ngRoute', 'ngAnimate', 'wc.directives', 'ui.bootstrap', 'breeze.angular']);

    Pray.config(['$routeProvider', function ($routeProvider) {
        var viewBase = '/prayer-wall/templates/';

        $routeProvider
            .when('/newrequest', {
                controller: 'CustomersController',
                templateUrl: viewBase + 'request.html',
                controllerAs: 'pw'
            })
            .otherwise({ redirectTo: '/' });

    }]);

}());