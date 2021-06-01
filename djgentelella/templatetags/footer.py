from django import template
from djgentelella.models import PermissionsCategoryManagement
from django.urls import resolve, reverse

register = template.Library()

@register.simple_tag
def get_page_name(val):
    #url = resolve(request.path_info).url_name
    url = reverse('permissionsmanagement-list')
    return url+'?q='+val

@register.simple_tag(takes_context=True)
def define_urlname_action(context, val):
    if not hasattr(context['request'], 'urlnamecontext'):
        setattr(context['request'],  'urlnamecontext', [])
    context['request'].urlnamecontext.append(val)
    return ""

@register.simple_tag(takes_context=True)
def get_urlname_action(context):
    value = getattr(context['request'], 'urlnamecontext', [])
    return ",".join(value)