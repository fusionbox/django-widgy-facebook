from itertools import islice
import datetime

from django.db import models

import facebook
import requests

from fusionbox.decorators import cached

import widgy
from widgy.models import Content

@widgy.register
class FacebookPosts(Content):
    editable = True

    target = models.CharField(max_length=255,
                              help_text="Whose posts do you want to show?", default='')

    count = models.PositiveIntegerField(default=4,
                                        help_text="How many posts do you want to show?")
    app_id = models.CharField(max_length=255,
                              help_text="Found in the Facebook app dashboard.")
    app_secret = models.CharField(max_length=255,
                                  help_text="Found in the same place as the app id.")

    def render(self, context, template=None):
        posts = self.get_posts()
        with context.push({'posts': posts}):
            return super(FacebookPosts, self).render(context, template)

    @cached(lambda self: [self.target, str(self.count)], timeout=datetime.timedelta(minutes=60))
    def get_posts(self):
        access_token = "{}|{}".format(self.app_id, self.app_secret)
        graph = facebook.GraphAPI(access_token)
        target_obj = graph.get_object(self.target)
        first_post_page = graph.get_connections(target_obj['id'], 'posts',
                                                fields="id, message, picture")
        return list(islice(self.post_gen(first_post_page), self.count))

    def post_gen(self, posts):
        while True:
            for post in posts['data']:
                yield post
            try:
                next_url = posts['paging']['next']
                posts = requests.get(next_url).json()
            except KeyError:
                break
