from django.db import models

class Today(models.Model):

    vorcher_no = models.PositiveIntegerField()

    date_dist = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Voucher {self.vorcher_no} on {self.date_dist}"

class Money(models.Model):
    PRICE_CHOICES = [
        ('v_1K', '1K'),
        ('v_1.5k', '1.5K'),
        ('v_6k', '6K'),
        ('v_25k', '25K')
    ]
    price_type = models.CharField(max_length=10, choices=PRICE_CHOICES)
    vorcher_received = models.PositiveIntegerField()
    vorcher_sold = models.PositiveIntegerField()
    vorcher_remaining = models.PositiveIntegerField(editable=False, default=0)

    def save(self, *args, **kwargs):
        self.vorcher_remaining = self.vorcher_received - self.vorcher_sold
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.price_type}: Received {self.vorcher_received}, Sold {self.vorcher_sold}, Remaining {self.vorcher_remaining}"
