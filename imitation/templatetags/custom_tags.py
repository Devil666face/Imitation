from config.settings import STATIC_ROOT
from django.template import Library
from datetime import datetime

register = Library()


@register.inclusion_tag('imitation/include/navbar.html')
def show_navbar(request):
    current_page = request.get('PATH_INFO')
    return {'current_page': current_page}


# @register.simple_tag(name='get_str_month')
# def get_str_month(month_number):
#     return datetime(datetime.today().year, month_number, 1).strftime("%B")
