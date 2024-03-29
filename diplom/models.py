import time
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime, timedelta

# Create your models here.
class CustomUser(AbstractUser):
    courier = models.OneToOneField(
        "Courier",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Курьер",
    )
    vendor = models.OneToOneField(
        "Vendor",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Заказчик",
    )

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Courier(models.Model):
    name = models.CharField(max_length=12, verbose_name="Имя курьера")
    drivingExperience = models.PositiveIntegerField(verbose_name="Водительский стаж")
    number = models.CharField(max_length=17, unique=True, verbose_name="Номер телефона")

    class Meta:
        verbose_name = "Курьер"
        verbose_name_plural = "Курьеры"

    def __str__(self):
        return self.name


class Order(models.Model):
    STATE_CHOICES = [
        ("1", "Обрабатывается"),
        ("2", "Подготавливают"),
        ("3", "Готов"),
    ]
    IDVendor = models.ForeignKey(
        "Vendor", on_delete=models.CASCADE, verbose_name="Заказчик"
    )
    IDCourier = models.ForeignKey(
        "CustomUser",
        on_delete=models.CASCADE,
        verbose_name="Курьер",
        null=True,
        blank=True,
    )
    date = models.DateField(verbose_name="Дата и время создания", auto_now_add=True)
    address = models.CharField(max_length=50, verbose_name="Адрес")
    deliverTo = models.DateTimeField(verbose_name="Доставить до", blank=True, default=datetime.now()+timedelta(minutes=45))
    state = models.CharField(
        max_length=255,
        choices=STATE_CHOICES,
        default="1",
        verbose_name="Состояние",
    )
    phoneNumber = models.CharField(max_length=17, verbose_name="Телефон для связи")
    review = models.TextField(null=True, blank=True, verbose_name="Комментарий")




    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Vendor(models.Model):
    address = models.CharField(max_length=50, verbose_name="Адрес")
    nameOfOrganization = models.CharField(
        max_length=30, verbose_name="Название организации"
    )

    class Meta:
        verbose_name = "Заказчик"
        verbose_name_plural = "Заказчики"

    def __str__(self):
        return self.nameOfOrganization
