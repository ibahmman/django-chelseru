from django.db import models


class Seru(models.Model):
    RESULT_CHOICES = [
        (1, 'khaas'),
        (2, 'minjaa'),
        (3, 'ga`n'),
    ]

    lu = models.TextField(verbose_name='luri', blank=False, null=False)
    pe = models.TextField(verbose_name='parsi', blank=False, null=False)
    result = models.IntegerField(verbose_name='natije', default=1, choices=RESULT_CHOICES)
    sound = models.FileField(verbose_name='dang', blank=True, null=True)