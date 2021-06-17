from django.db import models

class Image(models.Model):
    img=models.CharField(max_length=10000000)

    def __str__(self):
        return f"{self.id}___{self.img}"

class ImageSuccess(models.Model):
    icn=models.CharField(max_length=10000000)

    def __str__(self):
        return f"{self.id}___{self.icn}"

class Details(models.Model):
    name=models.CharField(max_length=1000)
    amount=models.CharField(max_length=100)
    payment_id=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    paid=models.BooleanField(default=False)

    # def __str__(self):
    #     return {
    #         "name": self.name,
    #         "email":self.email,
    #         "amount":self.amount,
    #         "payment id": self.payment_id,
    #         "payment status": self.paid,
    #     }
