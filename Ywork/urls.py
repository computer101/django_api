from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),

    # Home page
    path('', views.home, name='home'),

    # Profile page (requires login)
    path('profile/', views.profile, name='profile'),

    # allauth URLs (login, logout, callback, etc.)
    path('accounts/', include('allauth.urls')),
]
