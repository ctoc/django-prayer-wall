(function () {

    var injectParams = ['$location', '$routeParams'];

    var PrayerController = function ($location, $routeParams) {
        var pw = this,
            path = '/';

        pw.newrequest = function () {
        };
    };

    angular.module('prayerApp')
        .controller('PrayerController', PrayerController);

}());