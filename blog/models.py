from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    autor = models.ForeignKey('auth.user', on_delete = models.CASCADE)
    title = models.CharField(max_length = 200)
    text = models.TextField()
    fecha_de_creacion = models.DateTimeField(default = timezone.now)
    fecha_de_publicacion = models.DateTimeField(blank = True, null = True)

    def publicar(self):
        self.fecha_de_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.title