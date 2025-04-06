from django.db import models
from django.contrib.auth.models import User

class Expense(models.Model):
    CATEGORIES = [
        ('FOOD', 'Food'),
        ('TRANSPORTATION', 'Transportation'),
        ('BILLS','Bills')
        ('ENTERTAINMENT', 'Entertainment'),
        ('OTHER','Other'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=1, decimal_places=2)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.category} - {self.amount}"
# Create your models here.
