<<<<<<< HEAD
from django import template

register = template.Library()

@register.filter
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
=======
from django import template

register = template.Library()

@register.filter
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()
>>>>>>> 15be31861fda91f6cf1e88c672e9545593538aa4
