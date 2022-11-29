from django.urls import path
from store.views.views import *

app_name = 'store'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]