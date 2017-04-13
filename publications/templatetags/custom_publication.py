from django import template


register = template.Library()


@register.filter(is_safe=True)
def custom_datetime(value):
    return value.strftime("%d.%m.%Y %H:%M:%S")