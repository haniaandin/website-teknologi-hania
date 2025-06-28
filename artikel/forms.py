from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from django.contrib.auth.models import User
from artikel.models import Kategori, Artikel


class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Masukkan Nama Kategori'
            }),
        }


class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['kategori', 'judul', 'isi', 'gambar', 'status']
        widgets = {
            'kategori': forms.Select(attrs={'class': 'form-control'}),
            'judul': forms.TextInput(attrs={
                'class': 'form-control',
                'required': True,
                'placeholder': 'Masukkan Judul Artikel'
            }),
            'isi': CKEditor5Widget(attrs={'class': 'django_ckeditor_5'}, config_name='extends'),
            'gambar': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'is_staff']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama depan',
                'required': True
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama belakang'
            }),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
