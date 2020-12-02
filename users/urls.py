from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_v
app_name='users'

urlpatterns = [
    path('',include('django.contrib.auth.urls')),
    path('register',views.register,name='register'),
    path('change_password/',auth_v.PasswordChangeView.as_view(),name='password_password'),
    path('password_change_done/', auth_v.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('reset_password', auth_v.PasswordResetView.as_view(), name='reset_password'),
    path('reset/<uidb64>/<token>/',auth_v.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_done', auth_v.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/',auth_v.PasswordResetView.as_view(),name='password_reset'),
    path('reset/done/',auth_v.PasswordResetCompleteView.as_view(),name='password_reset_complete'),

              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
