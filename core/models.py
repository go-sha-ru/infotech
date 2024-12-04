from django.db import models


class Data(models.Model):
    ne = models.CharField(max_length=10, verbose_name='Базовая станция', unique=True)
    address = models.CharField(max_length=128, verbose_name="Адрес", null=True, blank=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    gsm = models.BooleanField(default=False)
    umts = models.BooleanField(default=False)
    lte = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.ne

    def coordinates(self) -> str:
        return f'{self.latitude}, {self.longitude}'

    def technology(self) -> str:
        ret = []
        if self.gsm:
            ret.append('gsm')
        if self.lte:
            ret.append('lte')
        if self.umts:
            ret.append('umts')
        return ', '.join(ret)

    class Meta:
        verbose_name = 'Базовая станция'
        verbose_name_plural = 'Базовые станции'
