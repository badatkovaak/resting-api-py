from django.http import HttpResponse
from django.template import loader


def home(request):
    return HttpResponse(loader.get_template("base.html").render({}, request))
