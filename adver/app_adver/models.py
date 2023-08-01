from django.db import models

# Create your models here.
class Advers(models.Model):
    title = models.CharField("Title", max_length=60)
    description = models.TextField("description")
    price = models.DecimalField("price", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("date_of_create", auto_now_add=True)
    updated_At = models.DateTimeField("date_of_change", auto_now=True)
    is_auction = models.BooleanField("is_Auction", help_text="choose, if it's auction")
    
    class Meta:
        db_table = "Advers"

    def __str__(self):
        return f"Advers(id={self.id}, title={self.title}, is_auction={self.is_auction})"