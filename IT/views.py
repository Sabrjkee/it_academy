from django.views.generic import DetailView

from IT import utils
from main_site.models import MO


class EqipmentView(DetailView):
    template_name = 'it/equipment.html'
    model = MO


class NetworkView(DetailView):
    template_name = 'it/network.html'
    model = MO


class ProviderView(DetailView):
    template_name = 'it/provider.html'
    model = MO


