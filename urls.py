from django.contrib import admin
from django.urls import include,path
from dango.contrib.auth import views as auth_views
from . import contact

urlpatterns=[
    path('admin/',admin.site.urls),
    path('contact/',contact.contact,name='contact'),]