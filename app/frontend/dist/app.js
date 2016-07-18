(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
angular.module('myapp', ['ngRoute', 'ngResource', 'ngNamedRoute', 'dcbImgFallback']).config(["$routeProvider", "$locationProvider", function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);
    $routeProvider.otherwise({
        redirectTo: '/'
    });
}]).controller('HeaderController', ["$scope", "$location", function ($scope, $location) {

    $scope.isActive = function (viewLocation) {
        return viewLocation === $location.path();
    };
}]).filter('startFrom', function () {
    return function (input, start) {
        start = +start; //parse to int
        return input.slice(start);
    };
});
require('./sample');

},{"./sample":2}],2:[function(require,module,exports){
require('./routes');
require('./services');
require('./resources');

},{"./resources":3,"./routes":15,"./services":22}],3:[function(require,module,exports){
require('./resources-config');
require('./politician-resource');

},{"./politician-resource":4,"./resources-config":5}],4:[function(require,module,exports){
angular.module('myapp').factory('Politician', ['$resource', function ($resource) {
    return $resource('/api/politicians/:slug', { slug: '@slug' }, {
        'list': { method: 'GET', isArray: true },
        'update': { method: 'PUT' }
    });
}]);

},{}],5:[function(require,module,exports){
angular.module('myapp').config(["$resourceProvider", function ($resourceProvider) {
    $resourceProvider.defaults.stripTrailingSlashes = false;
}]);

},{}],6:[function(require,module,exports){
angular.module('myapp').controller('AboutController', ["$scope", function ($scope) {}]);

},{}],7:[function(require,module,exports){
angular.module('myapp').config(["$routeProvider", function ($routeProvider) {
    $routeProvider.when('/about', {
        name: 'about',
        templateUrl: 'sample/routes/about/about.html',
        controller: 'AboutController',
        controllerAs: 'ctrl'
    });
}]);

},{}],8:[function(require,module,exports){
require('./about-controller');
require('./about-routes');

},{"./about-controller":6,"./about-routes":7}],9:[function(require,module,exports){
angular.module('myapp').controller('ContactController', ["$scope", function ($scope) {}]);

},{}],10:[function(require,module,exports){
angular.module('myapp').config(["$routeProvider", function ($routeProvider) {
    $routeProvider.when('/contact', {
        name: 'contact',
        templateUrl: 'sample/routes/contact/contact.html',
        controller: 'ContactController',
        controllerAs: 'ctrl'
    });
}]);

},{}],11:[function(require,module,exports){
require('./contact-controller');
require('./contact-routes');

},{"./contact-controller":9,"./contact-routes":10}],12:[function(require,module,exports){
angular.module('myapp').controller('HomeController', ["$scope", "orderByFilter", "Politician", function ($scope, orderByFilter, Politician) {
    var politicians = Politician.list();

    politicians.$promise.then(function (result) {
        $scope.orderedPoliticians = orderByFilter(result, "-stats.total");
    });
}]);

},{}],13:[function(require,module,exports){
angular.module('myapp').config(["$routeProvider", function ($routeProvider) {
    $routeProvider.when('/', {
        name: 'home',
        templateUrl: 'sample/routes/home/home.html',
        controller: 'HomeController',
        controllerAs: 'ctrl'
    });
}]);

},{}],14:[function(require,module,exports){
require('./home-controller');
require('./home-routes');

},{"./home-controller":12,"./home-routes":13}],15:[function(require,module,exports){
require('./home');
require('./rank');
require('./politician');
require('./contact');
require('./about');

angular.module('myapp').run(["$rootScope", "namedRouteService", function ($rootScope, namedRouteService) {
    $rootScope.$on('$routeChangeError', function (ev, current, previous, rejection) {
        if (rejection.status === 404) {
            alert('Not found');
            namedRouteService.open('home');
        }
    });
}]);

},{"./about":8,"./contact":11,"./home":14,"./politician":16,"./rank":19}],16:[function(require,module,exports){
require('./politician-controller');
require('./politician-routes');

},{"./politician-controller":17,"./politician-routes":18}],17:[function(require,module,exports){
angular.module('myapp').controller('PoliticianController', ["$scope", "PoliticianData", "Politician", function ($scope, PoliticianData, Politician) {

    $scope.politicianData = new Politician(PoliticianData);
    console.log($scope.politicianData);
}]);

},{}],18:[function(require,module,exports){
angular.module('myapp').config(["$routeProvider", function ($routeProvider) {
    $routeProvider.when('/politician/:slug', {
        name: 'politician',
        templateUrl: 'sample/routes/politician/politician.html',
        controller: 'PoliticianController',
        controllerAs: 'ctrl',
        resolve: {
            PoliticianData: ["Politician", "$route", function (Politician, $route) {
                var politicianData = Politician.get({
                    slug: $route.current.params.slug
                });
                return politicianData.$promise;
            }]
        }
    });
}]);

},{}],19:[function(require,module,exports){
require('./rank-controller');
require('./rank-routes');

},{"./rank-controller":20,"./rank-routes":21}],20:[function(require,module,exports){
angular.module('myapp').controller('RankController', ["$scope", "Politician", "orderByFilter", "$location", function ($scope, Politician, orderByFilter, $location) {
    $scope.currentPage = 0;
    $scope.pageSize = 10;
    $scope.rankBy = "-stats.total";
    $scope.politicians = Politician.list();

    $scope.politicians.$promise.then(function (result) {
        $scope.politicians = result;
        buildPagination();
        $scope.rank();
        console.log($scope.politicians);
    });

    var getItems = function () {
        var items = $scope.politicians;
        if ($scope.query && $scope.filtered.length > 0) {
            items = $scope.filtered;
        }
        return items;
    };

    var buildPagination = function () {

        $scope.numberOfPages = new Array(Math.ceil(getItems().length / $scope.pageSize));
    };

    $scope.rank = function () {
        $scope.politicians = orderByFilter($scope.politicians, $scope.rankBy);
    };

    $scope.changePage = function (page) {
        if (page >= 0 && page <= getItems().length / $scope.pageSize) {
            $scope.currentPage = page;
        }
    };

    $scope.go = function (politician) {
        $location.path('/politician/' + politician.slug);
    };

    $scope.search = function (item) {
        var found = false;
        var fullName = item.first_name + " " + item.last_name;
        if (!$scope.query || item.first_name.toLowerCase().indexOf($scope.query.toLowerCase()) != -1 || item.last_name.toLowerCase().indexOf($scope.query.toLowerCase()) != -1 || fullName.toLowerCase().indexOf($scope.query.toLowerCase()) != -1) {

            found = true;
        }

        buildPagination();

        return found;
    };

    $scope.hasNext = function () {
        return $scope.currentPage >= getItems().length / $scope.pageSize - 1;
    };
}]);

},{}],21:[function(require,module,exports){
angular.module('myapp').config(["$routeProvider", function ($routeProvider) {
    $routeProvider.when('/rank', {
        name: 'rank',
        templateUrl: 'sample/routes/rank/rank.html',
        controller: 'RankController',
        controllerAs: 'ctrl'
    });
}]);

},{}],22:[function(require,module,exports){

},{}]},{},[1]);

//# sourceMappingURL=maps/app.js.map
