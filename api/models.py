from django.db import models
class BukuTamu(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    nama = models.CharField(max_length=100, blank=True, default='')
    alamat = models.TextField()
    nomortelepon = models.CharField(max_length=100, blank=True, default='')
    gambar = models.ImageField(upload_to='gambar')
# Create your models here.
    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.nama)