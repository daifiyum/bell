from django import template
from django.utils.safestring import mark_safe
from marko.ext.gfm import gfm

register = template.Library()

@register.filter(is_safe=True)
def mdc(value):
    converted_value = gfm.convert(value)
    return mark_safe(converted_value)