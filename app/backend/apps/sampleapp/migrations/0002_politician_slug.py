# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models, migrations
from django.utils.text import slugify


def slugifyPoliticians(apps, schema_editor):
    # We can't import the Person model directly as it may be a newer
    # version than this migration expects. We use the historical version.
    Politician = apps.get_model("sampleapp", "Politician")
    for politician in Politician.objects.all():
        base_slug = slug = slugify(politician.text)
        i = 1
        while (Task.objects.filter(slug=slug).exists()):
            slug = '%s%s' % (base_slug, i)
            i += 1
        politician.slug = slug
        politician.save()


class Migration(migrations.Migration):

    dependencies = [
        ('sampleapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='politician',
            name='slug',
            field=models.SlugField(default='slug'),
            preserve_default=False,
        ),
        migrations.RunPython(slugifyPoliticians)
    ]
