from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    protocol = 'https'  # http ya https
    def items(self):
        return [
            'home_urls:index_urls',
            'home_urls:signup_urls',
            'home_urls:signin_urls',
            'home_urls:logout_urls',
            'home_urls:dashboard_urls',
        ]

    def location(self, item):
        return reverse(item)

    def get_urls(self, site=None, **kwargs):
        from django.contrib.sites.models import Site
        site = Site(domain="vms.casemfc.com", name="vms.casemfc.com")
        return super().get_urls(site=site, **kwargs)
