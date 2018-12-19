from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from IT import utils
from main_site.models import MO



class EqipmentView(LoginRequiredMixin, DetailView):
    template_name = 'it/equipment.html'
    model = MO


class NetworkView(LoginRequiredMixin, DetailView):
    template_name = 'it/network.html'
    model = MO


class ProviderView(LoginRequiredMixin, DetailView):
    template_name = 'it/provider.html'
    model = MO


