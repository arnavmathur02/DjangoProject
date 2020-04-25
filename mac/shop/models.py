from django.db import models

# Create your models here.

class Products(models.Model):
    """Model definition for Products."""

    # TODO: Define fields here

    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
