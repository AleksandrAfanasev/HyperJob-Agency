from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('signup', SingupView.as_view(), name='signup'),
    path('vacancies/', VacanciesView.as_view()),
    path('home/', MainPageView.as_view(), name='main'),
    path('', MainPageView.as_view()),
    path('login/', RedirectView.as_view(url='/login')),
    path('logout/', RedirectView.as_view(url='/logout')),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('vacancy/new', NewVacancyView.as_view(), name='new_vacancy'),
]