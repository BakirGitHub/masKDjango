from django.db import models

# Create your models here.
class Product(models.Model):
	CATEGORY = (
		('for men', 'for men'),
		('for women', 'for women'),
		('for kids', 'for kids'),
		)
	
	name = models.CharField(max_length=30, null=True)
	image = models.ImageField(null=True, blank=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=30, null=True,choices=CATEGORY)
	description = models.CharField(max_length=30, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name

class Order(models.Model):
	first_name = models.CharField(max_length = 30, null=True)
	last_name = models.CharField(max_length=30, null=True)
	product = models.ForeignKey(Product, null=True ,on_delete=models.SET_NULL)
	SIZE = (
		('L','L'),
		('M','M'),
		('S','S'),
		)
	size = models.CharField(max_length=30, null=True, choices=SIZE)


	def __str__(self):
		return self.first_name