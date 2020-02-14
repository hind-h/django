from django import template

register = template.Library()

@register.filter(name='cut1')
def cut1(value, arg):
    return value.replace(arg,'')