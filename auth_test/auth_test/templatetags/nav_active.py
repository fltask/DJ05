from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, url_name):
    request = context['request']
    return 'active' if request.resolver_match.view_name == url_name else ''
