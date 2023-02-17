from django.contrib import admin
from django.urls import path, include

from core.views import frontpage, contact, viziune

urlpatterns = [
    path('', include('store.urls')),
    path('',frontpage,name='frontpage'),
    path('viziune/',viziune,name='viziune'),
    path('contact/',contact,name='contact'),
    path('admin/', admin.site.urls),
]
