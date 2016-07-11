from django.db import models
from django.utils.text import slugify

class TwitterStats(models.Model):
    total = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)
    positive = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)

class RssStats(models.Model):
    total = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)
    positive = models.IntegerField(default=0)
    neutral = models.IntegerField(default=0)

class Stats(models.Model):
    total = models.IntegerField(default=0)
    total_negative = models.IntegerField(default=0)
    total_positive = models.IntegerField(default=0)
    total_neutral = models.IntegerField(default=0)
    twitter = models.ForeignKey(TwitterStats,  on_delete=models.CASCADE, null=True, blank=True, default = None)
    rss = models.ForeignKey(RssStats, on_delete=models.CASCADE, null=True, blank=True, default = None)

class Politician(models.Model):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=100, null=True, blank=True, default="")
    gender = models.CharField(max_length=6, choices=GENDER)

    photo_url = models.CharField(max_length=500, null=True, blank=True, default="")
    party_profile_url = models.CharField(max_length=500, null=True, blank=True, default="")
    website_url = models.CharField(max_length=500, null=True, blank=True, default="")
    twitter_url = models.CharField(max_length=500, null=True, blank=True, default="")
    facebook_url = models.CharField(max_length=500, null=True, blank=True, default="")
    instagram_url = models.CharField(max_length=500, null=True, blank=True, default="")
    linkedin_url = models.CharField(max_length=500, null=True, blank=True, default="")
    youtube_url = models.CharField(max_length=500, null=True, blank=True, default="")
    snapchat_url = models.CharField(max_length=500, null=True, blank=True, default="")
    phone_1 = models.CharField(max_length=50, null=True, blank=True, default="")
    phone_2 = models.CharField(max_length=50, null=True, blank=True, default="")    
    constituency = models.CharField(max_length=100)
    party = models.CharField(max_length=100)
    
    stats = models.ForeignKey(Stats, on_delete=models.CASCADE, null=True, blank=True, default = None)
    
    slug =  models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slug = slugify(self.first_name + "-" + self.last_name)
            i = 1
            while (Politician.objects.filter(slug=slug).exists()):
                slug = '%s%s' % (base_slug, i)
                i += 1
            self.slug = slug
        super(Politician, self).save(*args, **kwargs)

class Upload(models.Model):
    upload = models.FileField()

    def __str__(self):
        return self.upload.name

