from django import template

register = template.Library()

def split(stringToSplit):
    splitted = stringToSplit.split(',')
    return splitted

register.filter('split', split)