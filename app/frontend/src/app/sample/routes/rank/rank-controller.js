angular.module('myapp')
    .controller('RankController', function($scope, Politician) {
        $scope.politicians = Politician.list();  
        console.log($scope.politicians);
    });
