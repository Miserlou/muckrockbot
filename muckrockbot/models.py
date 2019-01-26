# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import twitter
from django.db import models
from django.conf import settings
from muckrockbot import managers


class Request(models.Model):
    """
    A FOIA request at MuckRock
    """
    muckrock_id = models.IntegerField()
    title = models.CharField(max_length=2000)
    slug = models.CharField(max_length=2000)
    status = models.CharField(max_length=50)
    username = models.CharField(max_length=2000)
    datetime_submitted = models.DateTimeField(null=True)
    datetime_done = models.DateTimeField(null=True)
    absolute_url = models.CharField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tweet_id = models.CharField(blank=True, default="", max_length=500)
    # Managers
    objects = managers.TwitterQuerySet.as_manager()
    completed = managers.CompletedManager()
    submitted = managers.SubmittedManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "https://www.muckrock.com{}".format(self.absolute_url)

    def is_tweeted(self):
        if self.tweet_id:
            return True
        else:
            return False
    is_tweeted.boolean = True

    @property
    def twitter_url(self):
        return 'https://twitter.com/muckrockbot/status/{}/'.format(self.tweet_id)

    @property
    def tweet_prefix(self):
        if self.datetime_done:
            return 'Completed'
        else:
            return 'Submitted'

    @property
    def tweet_text(self):
        return '{}: "{}" by {}'.format(
            self.tweet_prefix,
            self.title,
            self.username
        )

    def post(self):
        if self.tweet_id:
            return False
        api = twitter.Api(
            consumer_key=settings.TWITTER_CONSUMER_KEY,
            consumer_secret=settings.TWITTER_CONSUMER_SECRET,
            access_token_key=settings.TWITTER_ACCESS_TOKEN_KEY,
            access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
        )
        status = api.PostUpdate(self.tweet_text + "\n\n" + self.get_absolute_url())
        self.tweet_id = status.id
        self.save()
