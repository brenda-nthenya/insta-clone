from django.conf import settings
from . import views
from django.contrib.auth import views as  auth_views
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name="register-authentication"),
    path('accounts/profile/',views.profile_info,name='profile'),
    path('profile_edit/', views.profile_edit, name='profile_edit'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('search', views.search_profile, name='search_profile'),
    path('edit/', views.profile_edit, name='edit'),
    path('add_comment/', views.CommentCreateView.as_view(),name='add_comment'),
    
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

    