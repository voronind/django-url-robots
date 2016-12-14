from django.shortcuts import render

from url_robots.utils import create_rules


def robots_txt(request, template='robots.txt'):
    rules = create_rules()
    content_type = 'text/plain; charset=utf-8'

    return render(request, template, {'rules': rules}, content_type=content_type)
