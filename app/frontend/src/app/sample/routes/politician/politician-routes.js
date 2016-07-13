angular.module('myapp').config(function($routeProvider) {
    $routeProvider.when('/politician/:slug', {
        name: 'politician',
        templateUrl: 'sample/routes/politician/politician.html',
        controller: 'PoliticianController',
        controllerAs: 'ctrl',
        resolve: {
            PoliticianData: function(Politician, $route) {
                var politicianData = Politician.get({
                    slug: $route.current.params.slug
                });
                return politicianData.$promise;
            }
        }
    });
});
