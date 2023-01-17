from config.settings import STATIC_ROOT
from django.template import Library
from datetime import datetime

register = Library()


@register.inclusion_tag('imitation/include/navbar.html')
def show_navbar(request, user):
    current_page = request.get('PATH_INFO')
    return {
        'current_page': current_page, 
        'user':user,
    }


@register.simple_tag(name='get_list')
def get_list(some_list:list, index):
    return some_list[index]
