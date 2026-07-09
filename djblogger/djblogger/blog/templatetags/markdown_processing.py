import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def markdown(value):
    """Convert markdown text to HTML."""
    return md.markdown(value, extensions=["markdown.extensions.fenced_code"])
