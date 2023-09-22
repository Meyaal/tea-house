from django.shortcuts import render
from products.models import Product
from django.http import HttpResponse


# Create your views here.
def home(request):
    """The view for the start page. Renders the index.html
    page which also extends the base.html
    """
    products = Product.objects.all()[:6]

    context = {
        "products": products,
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def notFound(request):
    return render(request, "404.html")


def privacy(request):
    return render(request, "privacy.html")


def robots_txt(request):
    content = """
    User-agent: *
    Disallow: /admin/

    Sitemap: https://8000-meyaal-teahouse-r9n8ty34ek6.ws-eu104.gitpod.io/sitemap.xml
    """
    return HttpResponse(content, content_type="text/plain")
