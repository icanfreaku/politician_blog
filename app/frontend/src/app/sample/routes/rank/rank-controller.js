angular.module('myapp')
    .controller('RankController', function($scope, Politician, orderByFilter, $location) {
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
            
            $scope.numberOfPages = new Array(Math.ceil(getItems().length/$scope.pageSize));
        };

        $scope.rank = function () {
            $scope.politicians = orderByFilter($scope.politicians, $scope.rankBy);
        };

        $scope.changePage = function (page) {
            if (page >= 0 && page <= (getItems().length/$scope.pageSize)) {
                $scope.currentPage = page;
            }
        };

        $scope.go = function (politician) {
            $location.path('/politician/' + politician.slug);     
        };

        $scope.search = function(item){
            var found = false;
            var fullName = item.first_name + " " + item.last_name;
            if (!$scope.query || (item.first_name.toLowerCase().indexOf($scope.query.toLowerCase()) != -1) || 
                (item.last_name.toLowerCase().indexOf($scope.query.toLowerCase()) != -1) || 
                (fullName.toLowerCase().indexOf($scope.query.toLowerCase()) != -1)) {

                found = true;
            }
            
            buildPagination();        
            
            return found;
        };

        $scope.hasNext = function () {
            return $scope.currentPage >= getItems().length/$scope.pageSize - 1;
        };



    });
