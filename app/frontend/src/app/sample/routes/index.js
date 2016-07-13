require('./home');
require('./rank');
require('./politician');
require('./contact');
require('./about');



angular.module('myapp').run(function($rootScope, namedRouteService) {
    $rootScope.$on('$routeChangeError', function(ev, current, previous, rejection) {
        if (rejection.status === 404) {
            alert('Not found');
            namedRouteService.open('home');
        }
    });
});