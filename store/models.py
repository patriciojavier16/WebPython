from django.db import models

# Create your models here.
class Store(models.Model):
    title=models.CharField(max_length=100, verbose_name="Titulo")
    image=models.ImageField(verbose_name="Imagen", upload_to="store")
    content=models.TextField(verbose_name="Contenido")
    price=models.CharField(max_length=20, verbose_name="Precio")
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated=models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="Tienda"
        verbose_name_plural="Sabores"
        ordering=["-created"]

    def __str__(self):
        return self.title