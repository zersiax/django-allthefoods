from django.views.generic import ListView, DetailView

from .models import Nomspot

class NomspotListView(ListView):
    model = Nomspot

