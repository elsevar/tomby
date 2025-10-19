from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import JsonResponse

# Create your views here.

def gitlab_webhook_for_reviews(request: HttpRequest):
    return JsonResponse({"status": "OK"})