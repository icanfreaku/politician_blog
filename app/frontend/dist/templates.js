(function(module) {
try {
  module = angular.module('myapp');
} catch (e) {
  module = angular.module('myapp', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('sample/routes/about/about.html',
    '<h1>About</h1>');
}]);
})();

(function(module) {
try {
  module = angular.module('myapp');
} catch (e) {
  module = angular.module('myapp', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('sample/routes/contact/contact.html',
    '<h1>Contact</h1>');
}]);
})();

(function(module) {
try {
  module = angular.module('myapp');
} catch (e) {
  module = angular.module('myapp', []);
}
module.run(['$templateCache', function($templateCache) {
  $templateCache.put('sample/routes/home/home.html',
    '<div class="row content">\n' +
    '    <div class="col-sm-12">\n' +
    '        <div class="row">\n' +
    '            <div class="col-sm-12">\n' +
    '                <!-- <div class="jumbotron">\n' +
    '                  <h1>Politician 360</h1>\n' +
    '                  <p>Where you can find current, meaningful and interesting information about your politicians. Look around and have fun!!</p>\n' +
    '                </div> --> \n' +
    '                <div id="header-slider" class="carousel slide" data-ride="carousel">\n' +
    '                    <ol class="carousel-indicators">\n' +
    '                        <li data-target="#header-slider" data-slide-to="0" class="active"></li>\n' +
    '                        <li data-target="#header-slider" data-slide-to="1"></li>\n' +
    '                        <li data-target="#header-slider" data-slide-to="2"></li>\n' +
    '\n' +
    '                    </ol>\n' +
    '                    <div class="carousel-inner" role="listbox">\n' +
    '\n' +
    '                        <!--                       image 1 on the slider-->\n' +
    '                        <div class="item active">\n' +
    '                            <img src="../../../../../../media/flag1.jpg" alt="Irish Flag" />\n' +
    '                            <div class="carousel-caption">\n' +
    '                                <h3>Ireland politics at a Glance</h3>\n' +
    '                            </div>\n' +
    '                        </div>\n' +
    '                        <!--                        image2 on the slider-->\n' +
    '                        <div class="item">\n' +
    '                            <img src="../../../../../../media/image4.jpg" alt="Irish Flag" />\n' +
    '                            <div class="carousel-caption">\n' +
    '                                <h3>Team-Politician 360</h3>\n' +
    '                            </div>\n' +
    '                        </div>\n' +
    '                        <!--                        image3 on the slider-->\n' +
    '                        <div class="item">\n' +
    '                            <img src="../../../../../../media/image5.jpg" alt="Irish Flag" />\n' +
    '                            <div class="carousel-caption">\n' +
    '                                <h3>All at one place</h3>\n' +
    '                            </div>\n' +
    '                        </div>\n' +
    '                    </div>\n' +
    '                    <a href="#header-slider" class="left carousel-control" role="button" data-slide="prev">\n' +
    '                        <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>\n' +
    '                    </a>\n' +
    '\n' +
    '                    <a href="#header-slider" class="right carousel-control" role="button" data-slide="next">\n' +
    '                        <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>\n' +
    '                    </a>\n' +
    '                </div>  \n' +
    '            </div>\n' +
    '        </div>\n' +
    '        <div class="row">\n' +
    '            <div class="col-sm-4">\n' +
    '                <div class="panel panel-warning">\n' +
    '                  <div class="panel-heading">Latest News Articles</div>\n' +
    '                  <div class="panel-body">\n' +
    '                    Panel content\n' +
    '                  </div>\n' +
    '                </div>\n' +
    '            </div>\n' +
    '            <div class="col-sm-4">\n' +
    '                <div class="panel panel-warning">\n' +
    '                    <div class="panel-heading">Latest Tweets</div>\n' +
    '                    <div class="panel-body">\n' +
    '                        \n' +
    '                    </div>\n' +
    '                </div>\n' +
    '            </div>\n' +
    '            <div class="col-sm-4 top10">\n' +
    '                <div class="panel panel-warning">\n' +
    '                    <div class="panel-heading">Top 10 most popular politicians</div>\n' +
    '                    <div class="panel-body">\n' +
    '                        <div class="list-group text-left">\n' +
    '                          <a href="/politician/{{politician.slug}}" class="list-group-item" ng-repeat="politician in orderedPoliticians | limitTo:10">\n' +
    '                            <span class="badge pull-left">{{$index+1}}</span>\n' +
    '                            <img class="thumbnail" src="{{politician.photo_url}}" ng-if="politician.photo_url"/>\n' +
    '                            <img class="thumbnail" src="http://findicons.com/files/icons/703/artists_valley_sample/128/business_man_blue.png" ng-if="!politician.photo_url"></span>\n' +
    '                            <span>{{politician.first_name}} {{politician.last_name}}</span>\n' +
    '                          </a>\n' +
    '                        </div>    \n' +
    '                    </div>\n' +
    '                </div>\n' +
    '            </div>    \n' +
    '        </div>\n' +
    '    </div>\n' +
    '</div>  \n' +
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
  $templateCache.put('sample/routes/politician/politician.html',
    '<html>\n' +
    '<head>\n' +
    '<link href="https://file.myfontastic.com/n6vo44Re5QaWo8oCKShBs7/icons.css" rel="stylesheet">\n' +
    '<link rel="stylesheet" media="screen" href="https://fonts.googleapis.com/css?family=Roboto" />\n' +
    '<style>\n' +
    '.container {\n' +
    '    position: relative;\n' +
    '}\n' +
    '</style>\n' +
    '</head>\n' +
    '<body>\n' +
    '<div class="content-wrapper bg-orange">\n' +
    '  <div class="container">\n' +
    '    <div class="col-xs-12 candidates-header">\n' +
    '    </div>\n' +
    '  </div>\n' +
    '</div>\n' +
    '<div class="content-wrapper bg-grey-white" align="left">\n' +
    '  <div class="container">\n' +
    '    <div class="col-xs-12 container single-candidate">\n' +
    '      <h1><font color="#FF8000">Candidate</font></h1>\n' +
    '      <div class="col-md-4">\n' +
    '        <div class="candidate-pic">\n' +
    '					<img class="thumbnail" src="{{politicianData.photo_url}}" ng-if="politicianData.photo_url"/>\n' +
    '          <img class="thumbnail" src="http://findicons.com/files/icons/703/artists_valley_sample/128/business_man_blue.png" ng-if="!politician.photo_url"></span>\n' +
    '\n' +
    '        </div>\n' +
    '        <div class="candidate-details">\n' +
    '          <h4>Name</h4>\n' +
    '          <h5>{{politicianData.first_name}} {{politicianData.last_name}}</h5>\n' +
    '          <h4>Gender</h4>\n' +
    '          <h5>{{politicianData.gender}}</h5>\n' +
    '        	  </div>\n' +
    '      </div>\n' +
    '      <div class="col-md-4">\n' +
    '        <h4>Party</h4>\n' +
    '        <h5>{{politicianData.party}}</h5>\n' +
    '        <h4>Constituency</h4>\n' +
    '        <h5>{{politicianData.constituency}}</h5>\n' +
    '        <h4>Official Party Website</h4>\n' +
    '        <h5>{{politicianData.party_profile_url}}</h5>\n' +
    '\n' +
    '      </div>\n' +
    '      <div class="col-md-4 candidate-contacts">\n' +
    '        <h4>Contact</h4>\n' +
    '        <h5>t: <a href="{{politicianData.phone_1}}">{{politicianData.phone_2}}</a></h5>\n' +
    '        <h5>t: <a href="{{politicianData.phone_2}}"></a>{{politicianData.phone_2}}</h5>\n' +
    '        <h5>e: <a href="mailto:{{politicianData.email}}">{{politicianData.email}}</a></h5>\n' +
    '        <h5>w: <a href="{{politicianData.website_url}}">{{politicianData.website_url}}</a></h5>\n' +
    '        <h4>Social</h4>\n' +
    '				<div class="socicon">\n' +
    '					<ul class="socicon-list">\n' +
    '						<li><a style="text-decoration: none" class="socicon-twitter" href="{{politicianData.twitter_url}}"></a></li>\n' +
    '    				<li><a style="text-decoration: none" class="socicon-facebook" href="{{politicianData.facebook_url}}"></a>&nbsp;</li>\n' +
    '    				<li><a style="text-decoration: none" class="socicon-linkedin" href="{{polticianData.linkedin_url}}"></a>&nbsp;</li>\n' +
    '    				<li><a style="text-decoration: none" class="socicon-youtube" href="{{polticianData.youtube_url}}"></a>&nbsp;</li>\n' +
    '    				<li><a style="text-decoration: none" class="socicon-instagram" href="{{politicianData.instagram_url}}"></a></li>\n' +
    '       		</ul>\n' +
    '		  	</div>\n' +
    '			</div>\n' +
    '    </div>\n' +
    '		<div class="row">\n' +
    '					<div class="col-sm-4">\n' +
    '							<div class="panel panel-default">\n' +
    '								<div class="panel-heading">Latest News Articles</div>\n' +
    '								<div class="panel-body">\n' +
    '									Panel content\n' +
    '								</div>\n' +
    '							</div>\n' +
    '					</div>\n' +
    '					<div class="col-sm-4">\n' +
    '							<div class="panel panel-default">\n' +
    '									<div class="panel-heading">Latest Tweets</div>\n' +
    '									<div class="panel-body">\n' +
    '									</div>\n' +
    '							</div>\n' +
    '					</div>\n' +
    '  </div>\n' +
    '</div>\n' +
    '</body>\n' +
    '</html>\n' +
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
  $templateCache.put('sample/routes/rank/rank.html',
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
