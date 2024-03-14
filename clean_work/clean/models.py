from django.db import models

class Offers(models.Model):
      title = models.CharField(max_length=100)
      desc = models.TextField(max_length=500)
      price = models.IntegerField()
      time = models.CharField(max_length=50)
      img = models.ImageField(blank=True, null=True, upload_to='media')

      def __str__(self):
            return self.title
      
class Customers(models.Model):
      name = models.CharField(max_length=100)
      text_customer = models.TextField(max_length=500)
      img = models.ImageField(blank=True, null=True)

      def __str__(self):
            return self.name

