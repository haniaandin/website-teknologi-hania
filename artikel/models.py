from django.db import models
from django.contrib.auth.models import User

class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Kategori"
        ordering = ['-created_at']

    def __str__(self):
        return self.nama


class Artikel(models.Model):
    STATUS_DRAFT = 'draft'
    STATUS_PUBLISHED = 'published'

    STATUS_CHOICES = [
        (STATUS_DRAFT, 'Draft'),
        (STATUS_PUBLISHED, 'Published'),
    ]

    judul = models.CharField(max_length=200)
    isi = models.TextField()
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, related_name='artikels')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=STATUS_DRAFT)
    gambar = models.ImageField(upload_to='artikel_images/', blank=True, null=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = "Artikel"

    def __str__(self):
        return self.judul
