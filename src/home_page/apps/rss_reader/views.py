import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response
import models


def show_feeds(request):
    rss_feeds = models.RSSFeed.objects.filter(user=request.user).all()
    return render_to_response('rss_reader/templates/main.html',
                              {'rss_feeds': rss_feeds})


def show_feed(request, feed_id):
    feed_id = int(feed_id)
    rss_feed = models.RSSFeed.objects.filter(user=request.user).get(pk=feed_id)
    last_updated = datetime.datetime.now()
    return render_to_response('rss_reader/templates/feed.html',
                              {'rss_feed': rss_feed,
                               'last_updated': last_updated})


def sample(request, sample_name):
    import os

    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'rss_samples/%s.xml' % sample_name)
    with open(path, 'r') as rss_sample:
        return HttpResponse(rss_sample.read(),
                            content_type='application/xhtml+xml')
