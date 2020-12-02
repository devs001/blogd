"""blogd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_v

from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from artical.sitemaps import Artical_sitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {
 'articals': Artical_sitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('artical.urls')),
    path('users',include('users.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/',include('allauth.urls')),
    path('reset/<uidb64>/<token>/', auth_v.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_change_done/', auth_v.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset_done', auth_v.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},name='django.contrib.sitemaps.views.sitemap'),
    path('reset/done/', auth_v.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

