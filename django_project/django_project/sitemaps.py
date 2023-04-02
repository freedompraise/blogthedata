from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from blog.models import Post
from blog.models import Category


class HomeSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return ["home"]

    def location(self, item):
        return reverse(item)


class PostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return Post.objects.all()

    def lastmod(self, obj):
        return obj.date_posted

    # def location() Django uses get_absolute_url() by default


class CategorySitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Category.objects.all()

    def lastmod(self, obj):
        latest_post = obj.post_set.latest("date_posted")
        return latest_post.date_posted


class WorksCitedSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.1

    def items(self):
        return ["works-cited"]

    def location(self, item):
        return reverse(item)


class privacyPolicySiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.1

    def items(self):
        return ["privacy"]

    def location(self, item):
        return reverse(item)


class PortfolioSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ["portfolio"]

    def location(self, item):
        return reverse(item)


class StatusPageSiteMap(Sitemap):
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return ["status"]

    def location(self, item):
        return reverse(item)
