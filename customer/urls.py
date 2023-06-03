from django.urls import path,include
from customer.views import *

urlpatterns = [
    path('get-customers',GetcustomerViews.as_view()),
    path('get-addresses',CustomerAdressViews.as_view()),
    path('get-addresses',CustomerDetailsAddressViews.as_view()),
]
