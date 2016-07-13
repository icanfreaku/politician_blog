angular.module('myapp').config(function($routeProvider) {
    $routeProvider.when('/rank', {
        name: 'rank',
        templateUrl: 'sample/routes/rank/rank.html',
        controller: 'RankController',
        controllerAs: 'ctrl',
    });
});
