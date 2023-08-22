from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
    """The view for the start page. Renders the index.html
    page which also extends the base.html
    """