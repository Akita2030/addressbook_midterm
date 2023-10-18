from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    path('', AddressListView.as_view(), name='address-list'),
    path('', AddressDetailView.as_view(), name='address-detail'),
    path('', AddressCreateView.as_view(), name='address-create'),
]

urlpatterns += staticfiles_urlpatterns()