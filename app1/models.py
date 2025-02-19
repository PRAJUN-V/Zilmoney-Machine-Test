from django.db import models

# Create your models here.
class Expense(models.Model):
    name = models.CharField(max_length=50)
    amount = models.FloatField()
    category = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name