from django.shortcuts import render
from django.views import generic
from .models import Author, Post


class BasePage(generic.TemplateView):
    """
    Views based on class shows main page
    """
    template_name = "base_page.html"


class IndexPageView(generic.ListView):
    """
    Views for representing list of new notes
    """
    model = Post


class FooterPartView(generic.TemplateView):
    """
    Footer view page
    """
    template_name = "footer.html"
