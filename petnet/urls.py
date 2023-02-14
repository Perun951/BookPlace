from django.contrib import admin
from django.urls import path

from core.views import frontpage, viziune, contact, actiune, adventura, fantezie, educatie, religie

urlpatterns = [
    path('',frontpage,name='frontpage'),
    path('viziune/',viziune,name='viziune'),
    path('contact/',contact,name='contact'),
    path('actiune/',actiune,name='actiune'),
    path('adventura/',adventura,name='adventura'),
    path('fantezie/',fantezie,name='fantezie'),
    path('educatie/',educatie,name='educatie'),
    path('religie/',religie,name='religie'),
    path('admin/', admin.site.urls),
]
