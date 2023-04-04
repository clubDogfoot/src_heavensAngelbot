from django.db import models

# Create your models here.

class Robot(models.Model):
    name=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
    ip=models.CharField(max_length=30)
    port=models.IntegerField()
    note=models.TextField(null=True, blank=True)



    def __str__(self):
        return f"[{self.pk}] {self.name}"