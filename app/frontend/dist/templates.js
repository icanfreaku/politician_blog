(function(module) {
try {
  module = angular.module('myapp');
} catch (e) {
  module = angular.module('myapp', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('sample/routes/home/home.html',
    '<div>\n' +
    '    <table class="table">\n' +
    '        <thead>\n' +
    '          <tr>\n' +
    '            <th>First Name</th>\n' +
    '            <th>Last Name</th>\n' +
    '            <th>Gender</th>\n' +
    '            <th>Constituency</th>\n' +
    '            <th>Party</th>\n' +
    '          </tr>\n' +
    '        </thead>\n' +
    '        <tbody>\n' +
    '          <tr ng-repeat="politician in politicians">  \n' +
    '            <td>{{politician.first_name}}</td>\n' +
    '            <td>{{politician.last_name}}</td>\n' +
    '            <td>{{politician.gender}}</td>\n' +
    '            <td>{{politician.constituency}}</td>\n' +
    '            <td>{{politician.party}}</td>\n' +
    '          </tr>\n' +
    '        </tbody>\n' +
    '    </table>\n' +
    '</div>    \n' +
    '\n' +
    '\n' +
    '\n' +
    '\n' +
    '');
}]);
})();

(function(module) {
try {
  module = angular.module('myapp');
} catch (e) {
  module = angular.module('myapp', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('sample/routes/task-edit/task-edit.html',
    '<div class="task-list panel panel-default">\n' +
    '	<div class="panel-heading">\n' +
    '		<h3 class="panel-title">Update task</h3>\n' +
    '	</div>\n' +
    '	<div class="panel-body">\n' +
    '		<form name="form" ng-submit="ctrl.update(form)">\n' +
    '			<div class="form-group"> \n' +
    '				<input type="text" placeholder="Enter a task..." ng-model="taskData.text" required="required" class="form-control"/>\n' +
    '				<button type="submit" ng-disabled="!form.$valid" class="btn btn-primary">Update task</button>\n' +
    '			</div>\n' +
    '		</form>\n' +
    '	</div>\n' +
    '</div>');
}]);
})();
