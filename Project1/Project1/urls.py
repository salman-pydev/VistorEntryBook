"""Project1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from Project1 import settings
from app import views

urlpatterns = [
    path('index/',TemplateView.as_view(template_name="index.html")),
    path('UserLogin/', TemplateView.as_view(template_name="UserLogin.html")),
    path('UserSignup/',TemplateView.as_view(template_name="UserSignup.html")),
    path('visitorEntryform/',TemplateView.as_view(template_name="visitorEntryForm.html")),
    path('Details/',views.Details),
    path('Login/',views.Login),
    path('VisitorData/',views.VisitorData),
    path('adminLogin/',TemplateView.as_view(template_name="adminLogin.html")),
    path('checkAdmin/',views.checkAdmin),
    path('viewVisitor/',views.viewVisitor),
    path('products/',TemplateView.as_view(template_name="products.html")),
    path('logout/',TemplateView.as_view(template_name="index.html"))
]
if settings.DEBUG:
   # urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)