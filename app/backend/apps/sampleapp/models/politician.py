from django.db import models
from django.utils.text import slugify

# Create your models here.

class Politician(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    constituency = models.CharField(max_length=30)
    party = models.CharField(max_length=30)
    slug =  models.SlugField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slug = slugify(self.last_name + self.first_name)
            i = 1
            while (Politician.objects.filter(slug=slug).exists()):
                slug = '%s%s' % (base_slug, i)
                i += 1
            self.slug = slug
        super(Politician, self).save(*args, **kwargs)