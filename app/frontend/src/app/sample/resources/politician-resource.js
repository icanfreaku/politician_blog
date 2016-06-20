angular.module('myapp').factory('Politician', ['$resource', function($resource) {
    return $resource('/api/politicians/:slug', {slug: '@slug'},
        {
            'list': {method: 'GET', isArray: true},
            'update': { method:'PUT' }
        });
    }
]);