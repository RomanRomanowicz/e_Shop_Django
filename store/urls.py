from django.urls import path
from store.views.message import *
from store.views.views import *

app_name = 'store'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/', shop_view, name='shop'),
    path('shop/<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('/<int:id>/message/', post_message, name='post_message'),
    path('contact_message/', contact_message, name='contact_message'),
]