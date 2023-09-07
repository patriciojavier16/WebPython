from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Profession(models.Model):
    name=models.CharField(max_length=50, verbose_name="Nombre")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Profesión"
        verbose_name_plural="Profesiones"
        ordering=["name"]

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    content=models.TextField(verbose_name="Contenido")
    image=models.ImageField(verbose_name="Imagen", upload_to="testimonial")
    author= models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    profesiones=models.ManyToManyField(Profession, verbose_name="Profesiones")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Entrada"
        verbose_name_plural="Entradas"
        ordering=["-created"]

    def __str__(self):
        return self.content

