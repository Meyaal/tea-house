from django.shortcuts import render
from products.models import Product


# Create your views here.
def home(request):
    """The view for the start page. Renders the index.html
    page which also extends the base.html
    """
    products = Product.objects.all()[:6]

    context = {
        'products': products,
    }
    return render(request, 'index.html', context)


def about(request):
    return render(request, 'about.html')


def products(request):
    return render(request, 'product.html')


def store(request):
    return render(request, 'store.html') 


def feature(request):
    return render(request, 'feature.html')


def blog(request):
    return render(request, 'blog.html')


def testimonial(request):
    return render(request, 'testimonial.html')


def notFound(request):
    return render(request, '404.html')


def contact(request):
    return render(request, 'contact.html')


def privacy(request):
    return render(request, 'privacy.html')