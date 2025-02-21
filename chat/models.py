from django.db import models

class Satellite(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nome')
    orbital_state = models.CharField(max_length=50, verbose_name='Estado Orbital')
    designation = models.CharField(max_length=50, verbose_name='Designação')
    orbit = models.CharField(max_length=50, verbose_name='Órbita')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Atualizado em')

    class Meta:
        ordering = ['name']
        verbose_name = 'Satélite'

    def __str__(self):
        return self.name