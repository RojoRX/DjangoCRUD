from django.db import models

# Create your models here.
import pymysql

pymysql.install_as_MySQLdb()

class MyModel(models.Model):
    my_field = models.CharField(max_length=255)
    my_fieldTwo = models.CharField(max_length=255)
   
