from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    """
    Represents a product that a user (seller) is selling.
    
    Attributes:
        seller (User): The user who owns the product.
        name (str): The name of the product.
        description (str): A short description of the product.
        price (float): The price of the product.
        file (FileField): A file associated with the product, typically for download.
        total_sales_amount (int): The total sales amount of the product.
        total_sales (int): The total number of times the product has been sold.
    """
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.FloatField()
    file = models.FileField(upload_to='uploads')
    total_sales_amount = models.IntegerField(default=0)
    total_sales = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns the string representation of the product.
        
        Returns:
            str: The name of the product.
        """
        return self.name


class OrderDetail(models.Model):
    """
    Represents the details of a customer's order.
    
    Attributes:
        customer_email (EmailField): The email of the customer who placed the order.
        product (Product): The product associated with this order.
        amount (int): The total amount of the order.
        stripe_payment_intent (str): Stripe's payment intent ID for tracking the transaction.
        has_paid (bool): Indicates if the order has been paid.
        created_on (DateTime): The timestamp when the order was created.
        updated_on (DateTime): The timestamp when the order was last updated.
    """
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    stripe_payment_intent = models.CharField(max_length=200)
    has_paid = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)
