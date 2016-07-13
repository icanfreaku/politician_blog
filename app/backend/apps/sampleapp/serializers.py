from rest_framework import serializers
from .models import Politician
from .models import Stats
from .models import RssStats
from .models import TwitterStats



class RssStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RssStats

class TwitterStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwitterStats

class StatsSerializer(serializers.ModelSerializer):

    rss = RssStatsSerializer()
    twitter = TwitterStatsSerializer()

    class Meta:
        model = Stats

class PoliticianSerializer(serializers.HyperlinkedModelSerializer):

    stats = StatsSerializer()

    class Meta:
        model = Politician
        read_only_fields = ('slug',)

