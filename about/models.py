from django.db import models

# Create your models here.
class About(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    image=models.ImageField(verbose_name="Imagen", upload_to="about")
    content=models.TextField(verbose_name="Contenido")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Acerca de"
        verbose_name_plural="Acerca de Nosotros"
        ordering=["-created"]

    def __str__(self):
        return self.title
