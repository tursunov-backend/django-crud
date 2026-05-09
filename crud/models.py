from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=127)
    description = models.TextField(default='', null=False, blank=True)
    amount = models.DecimalField(decimal_places=2, max_digits=10)

    def __str__(self):
        return self.name
    
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'amount': float(self.amount),
        }
    