angular.module('myapp')
    .controller('HomeController', function($scope, Politician) {
        $scope.politicians = Politician.list();
        console.log("politicians",$scope.politicians);
    });