angular.module('myapp')
    .controller('PoliticianController', function($scope, PoliticianData, Politician) {

        $scope.politicianData = new Politician(PoliticianData);
          console.log($scope.politicianData);

    });
