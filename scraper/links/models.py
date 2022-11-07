from django.db import models
from .utils import get_link_data
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    USERNAME_FIELD = 'username'
    def __str__(self):
        return self.username


class Link(models.Model):
    user        = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    title       = models.CharField(max_length=364, blank=True)
    url         = models.URLField()
    current_price = models.FloatField(blank=True)
    old_price   = models.FloatField(blank=True)
    price_difference = models.FloatField(blank=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        title, price = get_link_data(self.url)
        old_price = self.current_price
        if self.current_price:
            if price != old_price:
                diff = price - old_price
                self.price_difference = round(diff, 2)
                self.old_price = old_price
        else:
            self.old_price = 0
            self.price_difference = 0

        self.title = title
        self.current_price = price

        super().save(*args, **kwargs)