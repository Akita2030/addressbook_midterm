from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    path('', AddressListView.as_view(), name='address-list'),
    path('address/detail/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('address/create', AddressCreateView.as_view(), name='address-create'),
]

urlpatterns += staticfiles_urlpatterns()
