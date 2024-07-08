from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    categoryname=models.CharField(max_length=100,primary_key=True)
    categoryid=models.IntegerField()

    def __str__(self):
        return self.categoryname

class Product(models.Model):
    categoryname=models.ForeignKey(ProductCategory,on_delete=models.CASCADE)
    pid=models.IntegerField(primary_key=True)
    pname=models.CharField(max_length=100)
    pprice=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.pname













