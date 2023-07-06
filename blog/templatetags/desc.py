from django import template
import re

register = template.Library()

@register.filter()
def desc(value):
    pattern = re.compile(r'<.*?>')
    clean_text = re.sub(pattern, '', value)
    return clean_text