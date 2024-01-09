from django import template

register = template.Library()

@register.filter
def honor(val):
    return val + '様'
