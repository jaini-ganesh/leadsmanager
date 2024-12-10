from django.db import models

# Create your models here.

class leads(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True,max_length=100)
    phone=models.CharField(max_length=12,unique=True,blank=True,null=True)
    message=models.TextField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated','-created']

    def __str__(self):
        return self.name
