from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from artikel import views as artikel_views
from mysite.views import *
from mysite.authentication import login_view, logout, registrasi

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Halaman utama
    path('', welcome, name="welcome"),

    # Artikel Umum
    path('artikel/<int:id>/', detail_artikel, name="detail_artikel"),
    path('artikel-not-found/', not_found_artikel, name="not_found_artikel"),

    # Halaman Publik
    path('tech/', tech, name="tech"),
    path('kontak/', kontak, name="kontak"),

    # Artikel dari API eksternal
    path('artikel-teknologi/', artikel_views.artikel_teknologi, name='artikel_teknologi'),
    path('toko/', artikel_views.artikel_teknologi, name='toko'),

    # Dashboard & Artikel internal
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/artikel_list', artikel_list, name="artikel_list"),
    path('dashboard/', include("artikel.urls")),

    # Autentikasi
    path('auth-login', login_view, name="auth-login"),
    path('auth-logout', logout, name="logout"),
    path('auth-registrasi', registrasi, name="registrasi"),

    # CKEditor
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

# Static & Media (development only)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
