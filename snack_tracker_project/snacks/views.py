from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Snack


class SnacksListView(ListView):
    template_name = "snack_list.html"
    model = Snack
    context_object_name = "snacks_list"


class SnackDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack