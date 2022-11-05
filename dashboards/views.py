from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from pages.models import Appeal


# Create your views here.


class AppealList(LoginRequiredMixin, ListView):
    model = Appeal
    template_name = 'dashboards/index.html'


class AppealDetail(LoginRequiredMixin, DetailView):

    model = Appeal
    template_name = 'dashboards/detail_modal.html'
