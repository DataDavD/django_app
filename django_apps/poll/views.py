from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return HttpResponse("Hello, world. You're at the polls index. Made with love by DataDavD")


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're looking at question %s" % question_id)


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def votes(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
