angular.module('myapp', ['ngRoute', 'ngResource', 'ngNamedRoute', 'dcbImgFallback'])
.config(function($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);
    $routeProvider.otherwise({
        redirectTo: '/'
    });
})
.controller('HeaderController', function($scope, $location) {
    
    $scope.isActive = function (viewLocation) { 
        return viewLocation === $location.path();
    };
})
.filter('startFrom', function() {
    return function(input, start) {
        start = +start; //parse to int
        return input.slice(start);
    };
});
require('./sample');
