angular.module('myapp').config(function($routeProvider) {
    $routeProvider.when('/contact', {
        name: 'contact',
        templateUrl: 'sample/routes/contact/contact.html',
        controller: 'ContactController',
        controllerAs: 'ctrl',
    });
});
