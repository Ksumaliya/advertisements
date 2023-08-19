from django.db import models
from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.utils.safestring import mark_safe

User = get_user_model()
# Create your models here.
class Advers(models.Model):
    title = models.CharField("Title", max_length=60)
    description = models.TextField("description")
    price = models.DecimalField("price", max_digits=10, decimal_places=2)
    created_at = models.DateTimeField("date_of_create", auto_now_add=True)
    updated_at = models.DateTimeField("date_of_change", auto_now=True)
    is_auction = models.BooleanField("is_Auction", help_text="choose, if it's auction")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField('image', upload_to='advers', blank=True)

    @admin.display(description="image")
    def image_of_adv(self):
        if self.image:
            return format_html(f"<img scr = '{self.image.url}' width = '50px' height = '50px'>")
        return None

    @admin.display(description="date_of_create")
    def created_date(self):
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime("%H:%M:")
            return format_html(
                "<span style='color: green; font-weight: bold'>Сегодня в {}</span>", created_time
            )
        return self.created_at.strftime("%d.%m.%Y - %H:%M:")
    
    @admin.display(description="date_of_update")
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime("%H:%M:")
            return format_html(
                "<span style='color: gold; font-weight: bold'>Сегодня в {}</span>", updated_time
            )
        return self.updated_at.strftime("%d.%m.%Y - %H:%M:")
    
    class Meta:
        db_table = "Advers"

    def __str__(self):
        return f"Advers(id={self.id}, title={self.title}, is_auction={self.is_auction})"