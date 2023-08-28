from django.db import models

# Create your models here.
class Advertisment(models.Model):
    title = models.CharField('название', max_length=120)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    trades = models.BooleanField('торг', help_text='Если хотите торговаться')
    date_now = models.DateField("Создание дата", auto_now_add=True)
    date_update = models.DateField("Обновление дата", auto_now=True)

    class Meta:
        db_table = "advertisment"

    def __str__(self):
        #return self.title
        return f"Advertisment(id = {self.id}, title = {self.title}, price = {self.price})"
