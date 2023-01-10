from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.views.generic import (
    FormView,
    TemplateView,
    View,
    CreateView,
    DeleteView,
    UpdateView,
)
from django.urls import reverse_lazy
from imitation.models import (
    Incident,
    Category,
    ExampleIncident
)
from django.urls import reverse_lazy
from imitation.forms import (
    IncidentCreateForm,
    CategoryCreateForm,
    ExampleIncidentCreateForm,
)
from django.contrib import messages


class LoginMixin(LoginRequiredMixin):
    login_url = '/login/'


class IncidentMixin(LoginMixin, View):
    model = Incident
    form_class = IncidentCreateForm
    success_url = reverse_lazy('imitation:incident_create')
    template_name = 'base.html'


class CategoryMixin(LoginMixin, View):
    model = Category
    form_class = CategoryCreateForm
    success_url = reverse_lazy('imitation:category_create')
    template_name = 'base.html'


class ExampleIncidentMixin(LoginMixin, View):
    model = ExampleIncident
    form_class = ExampleIncidentCreateForm
    success_url = reverse_lazy('imitation:exampleincident_create')
    template_name = 'base.html'


class ModelFormListCreateView(CreateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = self.model.objects.all()
        return context


class ModelFormListUpdateView(UpdateView):
    invalid_redirect_url = None
    
    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return HttpResponseRedirect(self.invalid_redirect_url)
    
    

class MessageFormMixin(FormView):
    info_message = ''
    error_message = ''

    def form_valid(self, form):
        messages.success(self.request, self.info_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return super().form_invalid(form)
    

class DeleteAjaxMixin(DeleteView):
    template_name = 'base.html'
    delete_message = ''

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        messages.success(request, self.delete_message)
        return HttpResponse(request)
