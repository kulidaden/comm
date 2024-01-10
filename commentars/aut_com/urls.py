from django.urls import path
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from captcha.views import captcha_image

urlpatterns = [
    path('', views.register_author, name='register'),
    path('login/', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
    path('update_comment/<int:comment_id>/', views.update_comment, name='update_comment'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),
    path('captcha/', include('captcha.urls')),
    path('captcha-image/', captcha_image, name='captcha-image'),
    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)