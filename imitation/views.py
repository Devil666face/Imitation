import plotly.express
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from imitation.models import (
    Incident,
    Category,
    ExampleIncident
)
from django.views.generic import (
    DetailView,
    ListView,
    FormView,
    UpdateView,
    CreateView,
    DeleteView,
    TemplateView,
)
from imitation.mixin import (
    LoginMixin,
    IncidentMixin,
    CategoryMixin,
    ExampleIncidentMixin,
    MessageFormMixin,
    DeleteAjaxMixin,
    ModelFormListCreateView,
    ModelFormListUpdateView,
)
from imitation.forms import (
    IncidentCreateForm,
    CategoryCreateForm,
    ExampleIncidentCreateForm,
)
from django.contrib import messages
from imitation.utils import (
    get_main_chart,
    get_rounded_chart,
)

class HomeView(IncidentMixin, ListView):
    template_name = 'imitation/home.html'

    def get(self, request, *args, **kwargs):
        self.update = bool(int(request.GET.get('update',1)))
        if self.update:
            messages.success(request, 'Автообновление включено. Период обновления 5 сек.')
        else:
            messages.warning(request, 'Автообновление отключено.')
            
        return super().get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['update'] = self.update
        context['stat_dict'] = IncidentAjaxStatisticView.get_stat_dict()
        return context


class StatisticView(LoginMixin, TemplateView):
    template_name = 'imitation/stat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stat_dict'] = IncidentAjaxStatisticView.get_stat_dict()
        context['chart'] = get_main_chart()
        if not context['chart']:
            messages.warning(self.request, 'Не создано не одного инцидента')
        else:
            messages.success(self.request, 'Графики построены.')
        context['round_chart'] = get_rounded_chart(data = context['stat_dict'])
        return context


class ResultView(IncidentMixin, ListView):
    template_name = 'imitation/result.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        print(queryset)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        messages.success(self.request, 'Вычисляю результаты.')
        context['stat_dict'] = IncidentAjaxStatisticView.get_stat_dict()
        return context
    


class IncidentListAjaxView(IncidentMixin, ListView):
    template_name = 'imitation/incident_list'
    context_object_name = 'incident_list'


class IncidentCreateView(IncidentMixin, ModelFormListCreateView, MessageFormMixin):
    template_name = 'imitation/incident_form_list.html'
    info_message = 'Инцидент создан.'
    error_message = 'Ошибка создания инцидента, проверьте правильность заполнения полей.'


class IncidentUpdateAjaxView(IncidentMixin, ModelFormListUpdateView):
    info_message = 'Инцидент обновлен'
    error_message = 'Ошибка обновления инцидента. Проверьте правильность введенных данных.'
    template_name = 'imitation/form.html'
    invalid_redirect_url = reverse_lazy('imitation:incident_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        context['action_url'] = reverse_lazy('imitation:incident_update', kwargs={'pk':self.object.pk})
        return context


class IncidentUpdateLegalAjaxView(IncidentMixin, ModelFormListUpdateView):

    def form_valid(self, form):
        super().form_valid(form)
        return self.response_class(request=self.request, template='imitation/incident_list.html' ,context={'incident_list':Incident.objects.filter(pk=self.object.pk)})
    

class IncidentDeleteAjaxView(IncidentMixin, DeleteAjaxMixin):
    delete_message = 'Инцидент удален'


class IncidentAjaxStatisticView(IncidentMixin, TemplateView):
    template_name = 'imitation/incident_stat.html'

    @staticmethod
    def get_stat_dict():
        return {'all':Incident.objects.all().count(), 
                'legal':Incident.objects.filter(legal='YES').count(),
                'legal_none':Incident.objects.filter(legal='NONE').count(),
                'legal_no':Incident.objects.filter(legal='NO').count()}


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stat_dict'] = IncidentAjaxStatisticView.get_stat_dict()

        return context

class CategoryCreateView(CategoryMixin, ModelFormListCreateView, MessageFormMixin):
    template_name = 'imitation/category_form_list.html'
    info_message = 'Тип инцидентов создан.'
    error_message = 'Ошибка создания типа инцидентов, проверьте правильность заполнения полей.'


class CategoryUpdateAjaxView(CategoryMixin, ModelFormListUpdateView):
    info_message = 'Инцидент обновлен'
    error_message = 'Ошибка обновления инцидента. Проверьте правильность введенных данных.'
    template_name = 'imitation/form.html'
    invalid_redirect_url = reverse_lazy('imitation:category_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        context['action_url'] = reverse_lazy('imitation:category_update', kwargs={'slug':self.object.slug})
        return context


class CategoryDeleteAjaxView(CategoryMixin, DeleteAjaxMixin):
    delete_message = 'Категория удалена'    
    

class ExampleIncidentCreateView(ExampleIncidentMixin, ModelFormListCreateView, MessageFormMixin):
    info_message = 'Типовой инцидент создан'
    error_message = 'Ошибка создания типового инцидента, проверьте правильность заполнения полей.'
    template_name = 'imitation/exampleincident_form_list.html'


class ExampleIncidentUpdateAjaxView(ExampleIncidentMixin, ModelFormListUpdateView):
    info_message = 'Типовой инцидент обновлен'
    error_message = 'Ошибка обновления типового инцидента. Проверьте правильность введенных данных.'
    template_name = 'imitation/form.html'
    invalid_redirect_url = reverse_lazy('imitation:exampleincident_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object'] = self.object
        context['action_url'] = reverse_lazy('imitation:exampleincident_update', kwargs={'pk':self.object.pk})
        return context


class ExampleIncidentDeleteAjaxView(ExampleIncidentMixin, DeleteAjaxMixin):
    delete_message = 'Типовой инцидент удален'
