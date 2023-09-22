from django.contrib.sitemaps import Sitemap
from blog.models import BlogPost
from products.models import Product
from django.urls import reverse


class BlogPostSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return BlogPost.objects.all()

    def lastmod(self, obj):
        return obj.date


class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Product.objects.all()


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        # List of your static view names
        return [
            "home",
            "products",
            "add_product",
            "blog",
            "add_post",
            "about",
            "404",
            "privacy",
            "contact",
            "checkout",
            "cache_checkout_data",
            "webhook",
            "view_bag",
        ]

    def location(self, item):
        return reverse(item)
