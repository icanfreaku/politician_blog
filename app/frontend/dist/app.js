(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
angular.module('myapp', ['ngRoute', 'ngResource', 'ngNamedRoute']).config(["$routeProvider", "$locationProvider", function ($routeProvider, $locationProvider) {
    $locationProvider.html5Mode(true);
    $routeProvider.otherwise({
        redirectTo: '/'
    });
}]);
require('./sample');

},{"./sample":2}],2:[function(require,module,exports){
require('./routes');
require('./services');
require('./resources');

},{"./resources":3,"./routes":9,"./services":13}],3:[function(require,module,exports){
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
angular.module('myapp').controller('HomeController', ["$scope", "Politician", function ($scope, Politician) {
    $scope.politicians = Politician.list();
    console.log("politicians", $scope.politicians);
}]);

},{}],7:[function(require,module,exports){
angular.module('myapp').config(["$routeProvider", function ($routeProvider) {
    $routeProvider.when('/', {
        name: 'home',
        templateUrl: 'sample/routes/home/home.html',
        controller: 'HomeController',
        controllerAs: 'ctrl'
    });
}]);

},{}],8:[function(require,module,exports){
require('./home-controller');
require('./home-routes');

},{"./home-controller":6,"./home-routes":7}],9:[function(require,module,exports){
require('./task-edit');
require('./home');

angular.module('myapp').run(["$rootScope", "namedRouteService", function ($rootScope, namedRouteService) {
    $rootScope.$on('$routeChangeError', function (ev, current, previous, rejection) {
        if (rejection.status === 404) {
            alert('Not found');
            namedRouteService.open('home');
        }
    });
}]);

},{"./home":8,"./task-edit":10}],10:[function(require,module,exports){
require('./task-edit-controller');
require('./task-edit-routes');

},{"./task-edit-controller":11,"./task-edit-routes":12}],11:[function(require,module,exports){
angular.module('myapp').controller('TaskEditController', ["$scope", "TaskData", "Task", "namedRouteService", function ($scope, TaskData, Task, namedRouteService) {

    $scope.taskData = new Task(TaskData);

    this.update = function (form) {
        if (form.$valid) {
            $scope.taskData.$update().then(function () {
                namedRouteService.open('home');
            }, function () {
                alert('Error occured');
            });
        }
    };
}]);

},{}],12:[function(require,module,exports){
angular.module('myapp').config(["$routeProvider", function ($routeProvider) {
    $routeProvider.when('/task/:slug', {
        name: 'edit-task',
        templateUrl: 'sample/routes/task-edit/task-edit.html',
        controller: 'TaskEditController',
        controllerAs: 'ctrl',
        resolve: {
            TaskData: ["Task", "$route", function (Task, $route) {
                var taskData = Task.get({
                    slug: $route.current.params.slug
                });
                return taskData.$promise;
            }]
        }
    });
}]);

},{}],13:[function(require,module,exports){

},{}]},{},[1]);

//# sourceMappingURL=maps/app.js.map
