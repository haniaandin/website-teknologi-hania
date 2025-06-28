from django.urls import path
from . import views

from artikel.views import (
    artikel_list,
    artikel_tambah,
    artikel_update,
    artikel_delete,
    artikel_detail,

    admin_kategori_list,
    admin_kategori_tambah,
    admin_kategori_update,
    admin_kategori_delete,

    admin_artikel_list,
    admin_artikel_tambah,
    admin_artikel_update,
    admin_artikel_delete,

    admin_management_user_list,
    admin_management_user_edit
)

urlpatterns = [
    # Artikel Teknologi API
    path('artikel-teknologi/', views.artikel_teknologi, name='artikel_teknologi'),

    ########################### Fungsi untuk user biasa ##############
    path('artikel/list', artikel_list, name="artikel_list"),
    path('artikel/tambah', artikel_tambah, name="artikel_tambah"),
    path('artikel/update/<int:id_artikel>', artikel_update, name="artikel_update"),
    path('artikel/delete/<int:id_artikel>', artikel_delete, name="artikel_delete"),
    path('artikel/<int:id>/', artikel_detail, name='artikel_detail'),

    ########################### Fungsi dari operator ##############
    path('operator/kategori/list', admin_kategori_list, name="admin_kategori_list"),
    path('operator/kategori/tambah', admin_kategori_tambah, name="admin_kategori_tambah"),
    path('operator/kategori/update/<int:id_kategori>', admin_kategori_update, name="admin_kategori_update"),
    path('operator/kategori/delete/<int:id_kategori>', admin_kategori_delete, name="admin_kategori_delete"),

    path('operator/artikel/list', admin_artikel_list, name="admin_artikel_list"),
    path('operator/artikel/tambah', admin_artikel_tambah, name="admin_artikel_tambah"),
    path('operator/artikel/update/<int:id_artikel>', admin_artikel_update, name="admin_artikel_update"),
    path('operator/artikel/delete/<int:id_artikel>', admin_artikel_delete, name="admin_artikel_delete"),

    path('dashboard/user/', admin_management_user_list, name='admin_management_user_list'),
    path('dashboard/user/edit/<int:user_id>/', admin_management_user_edit, name='admin_management_user_edit'),
]
