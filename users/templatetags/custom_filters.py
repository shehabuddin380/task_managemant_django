from django import template
from datetime import datetime
from django.utils import timezone
register = template.Library()


@register.filter
def humanized_date(value):
    if value:
        today = datetime.now().date()
        value = timezone.localtime(value)
        if value.date() == today:
            return f"Today at {value.strftime('%I:%M %p')}"
        if value.date() == today.replace(day=today.day - 1):
            return f"Yesterday at {value.strftime('%I:%M %p')}"
        else:
            return f"{value.date().strftime('%B %d')}, {value.strftime('%I:%M %p')}"
    return "No login record available"


@register.filter(name='has_group')
def has_group(user, group_name):
    """Usage in template: {% if request.user|has_group:"Admin" %}"""
    if not user.is_authenticated:
        return False
    return user.groups.filter(name=group_name).exists()

@register.filter(name='has_group')
def has_group(user, group_name):
    if not user.is_authenticated:
        return False
    return user.groups.filter(name=group_name).exists()