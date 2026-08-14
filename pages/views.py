from django.views.generic import TemplateView
from django.shortcuts import HttpResponse, render

# Create your views here.
# Function Based Views vs. Class Based Views

class HomePageView(TemplateView):
    template_name = "pages/home.html"
class AboutPageView(TemplateView):
    template_name = "pages/about.html"
# Function Based Views
def contact_page(request):
    # return HttpResponse("Hellow World from a FBV")
    return render(request, "pages/contact.html")