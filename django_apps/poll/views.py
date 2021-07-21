from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Question


def index(request: HttpRequest) -> HttpResponse:
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "poll/index.html", context)


def detail(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're looking at question %s" % question_id)


def results(request: HttpRequest, question_id: int) -> HttpResponse:
    response = "You're looking at the results of question %s"
    return HttpResponse(response % question_id)


def votes(request: HttpRequest, question_id: int) -> HttpResponse:
    return HttpResponse("You're voting on question %s." % question_id)
