from django.db import models
from django.db.models import DecimalField, PositiveIntegerField
from decimal import Decimal

# Create your models here.

# I will have category and then connected foods





class Category(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='cafe/media/category/images/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Categories"


class Food(models.Model):
    """Overall, Foods that should be added to database"""
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='cafe/media/food/images/', blank=True, null=True)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    discount = models.PositiveIntegerField(default=0, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='food', null=True, blank=True)
    rating = models.FloatField(default=0, null=True, blank=True)
    def __str__(self):
        return f"Food name - {self.title}, \nCategory - {self.category.title}"

    @property
    def discounted_price(self):
        """Function for calculating discounted price"""
        try:
            if self.discount is not None: #If discount is not 0
                self.discount_price = self.price * Decimal(1 - self.discount/100)
                return Decimal(f"{self.discount_price}").quantize(Decimal("0.00"))
            return Decimal(f'{self.price}').quantize(Decimal('0.00'))

        except (TypeError,ValueError, AttributeError) as e:
            print(f"You can't calculate discounted price due to {e}")

        except Exception as e:
            print(f"An error occured: {e}")


    class Meta:
        verbose_name_plural = "Foods"