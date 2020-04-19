from django.db import models

class Address(models.Model):
    ip=models.CharField(max_length=20)

    def __str__(self):
        return self.ip
    class Meta:
        verbose_name_plural="Adress"
