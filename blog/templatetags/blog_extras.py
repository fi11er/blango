from django.contrib.auth import get_user_model
from django import template
from django.utils.html import format_html

user_model = get_user_model()
register = template.Library()


@register.filter
def author_details(user: user_model, current_user: user_model=None):
    if not isinstance(user, user_model):
        return ''
    if user == current_user:
        return format_html('<strong>me</strong>')
    if user.first_name and user.last_name:
        name = f'{user.first_name} {user.last_name}'
    else:
        name = user.username
    if user.email:
      result = format_html('<a href="mailto:{}">{}</a>', user.email, name)
    else:
      result = format_html(name)
    return result