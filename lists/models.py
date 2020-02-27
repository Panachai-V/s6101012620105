from django.db import models

# Create your models here.
class cal_his(models.Model):
    x_value = models.CharField(max_length=211111111111)
    y_value = models.CharField(max_length=211111111111)
    op_value = models.CharField(max_length=211111111111)
    res_value = models.CharField(max_length=211111111111)
    # def __str__(self):
    #        return self.

class get_his(models.Model):
    x_value = models.CharField(max_length=211111111111)
    y_value = models.CharField(max_length=211111111111)
    op_value = models.CharField(max_length=211111111111)
    res_value = models.CharField(max_length=211111111111)

class post_his(models.Model):
    x_value = models.CharField(max_length=211111111111)
    y_value = models.CharField(max_length=211111111111)
    op_value = models.CharField(max_length=211111111111)
    res_value = models.CharField(max_length=211111111111)