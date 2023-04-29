"""registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app1 import views
# from app1.views import SurveyRatingListView, SurveyRatingCreateView, SurveyRatingUpdateView, SurveyRatingDeleteView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
    path('home/', views.HomePage, name='home'),
    path('logout/', views.LogoutPage, name='logout'),
    path('evaluation/', views.evaluation, name='evaluation'),
    path('evaluation/<int:pk>/edit/',
         views.edit_evaluation, name='edit_evaluation'),
    path('evaluation/<int:pk>/delete/',
         views.delete_evaluation, name='delete_evaluation'),
    path('evaluation_list/',
         views.evaluation_list, name='evaluation_list'),
]
#     path('survey-rating/list/', SurveyRatingListView.as_view(),
#          name='survey_rating_list'),
#     path('survey-rating/create/', SurveyRatingCreateView.as_view(),
#          name='survey_rating_create'),
#     path('survey-rating/<int:pk>/update/',
#          SurveyRatingUpdateView.as_view(), name='survey_rating_update'),
#     path('survey-rating/<int:pk>/delete/',
#          SurveyRatingDeleteView.as_view(), name='survey_rating_delete'),
