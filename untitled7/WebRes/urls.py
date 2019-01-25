from django.urls import path
from WebRes.views import *
urlpatterns = [
    path('second_page', test1),
    path('third_page', test2),
    path('main_page', index),
    path('auth', login_user),
    path('logout', auth_user),
    path('fourth_test', test3),
    path('registration', registration)

]