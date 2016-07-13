angular.module('myapp').config(function($routeProvider) {
    $routeProvider.when('/about', {
        name: 'about',
        templateUrl: 'sample/routes/about/about.html',
        controller: 'AboutController',
        controllerAs: 'ctrl',
    });
});
