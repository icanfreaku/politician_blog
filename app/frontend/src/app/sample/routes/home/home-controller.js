angular.module('myapp')
    .controller('HomeController', function($scope, orderByFilter, Politician) {
        var politicians = Politician.list();  

        politicians.$promise.then(function (result) {
            $scope.orderedPoliticians = orderByFilter(result, "-stats.total");
        });
    });
