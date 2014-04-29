import urllib2
from django.db import models
from django import forms
from django.core.urlresolvers import reverse
from lxml import etree


class SitemapParser(object):
    def __init__(self):
        self.start_loc = False
        self.data_loc = None
        self.pages = []

    def start(self, tag, attrib):
        try:
            if tag[-3:] == 'loc':
                print('found loc')
                self.start_loc = True
        except IndexError:
            print('did not find loc')

    def end(self, tag):
        try:
            if tag[-3:] == 'loc' and self.start_loc:
                self.pages.append(WebsitePage(self.data_loc))
                self.start_loc = False
                self.data_loc = None
        except IndexError:
            print('did not find loc')

    def data(self, data):
        if self.start_loc:
            self.data_loc = data

    def close(self):
        return "closed!"


class WebsitePage(object):
    def __init__(self, link):
        self.link = link

    def get_health(self):
        try:
            resp = urllib2.urlopen(self.link)
            return resp.getcode() == 200
        except Exception:
            return False

    def __unicode__(self):
        return self.link


class WebsiteHealthChecker(models.Model):
    url = models.URLField()
    sitemap_url = models.URLField()
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('website', args=(self.id,))

    def get_links(self):
        sitemap_parser = SitemapParser()
        parser = etree.XMLParser(target=sitemap_parser)
        etree.parse(self.sitemap_url, parser)
        return sitemap_parser.pages

    def __unicode__(self):
        return u'%s' % self.name


class WebsiteHealthCheckerForm(forms.ModelForm):

    class Meta:
        model = WebsiteHealthChecker