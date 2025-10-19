from django.urls import path
from .views import gitlab_webhook_for_reviews

urlpatterns = [
    path('', gitlab_webhook_for_reviews, name='gitlab_webhook_for_reviews'),
]