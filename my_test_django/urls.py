from django.urls import path

from .views import ArticleView
from . import views

app_name = 'my_test_django'

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('articles/', ArticleView.as_view()),
    path('articles/<int:pk>', ArticleView.as_view()),
]