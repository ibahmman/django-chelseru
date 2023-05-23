from django.db import models
from accounts.models import JobCategory, Skill


class Project(models.Model):
    title = models.CharField(verbose_name='شرح', max_length=70)
    more = models.TextField(verbose_name='بیشتر شرح دهید', blank=False)
    categories = models.ManyToManyField(JobCategory, verbose_name='دسته بندی ها', blank=True)
    skills = models.ManyToManyField(Skill, verbose_name='مهارت ها', blank=True)

    country_code = models.CharField(verbose_name='کد کشور', max_length=5)
    mobile = models.CharField(verbose_name='موبایل', max_length=10)
    email = models.EmailField(verbose_name='ایمیل')
    created_at = models.DateTimeField('زمان سفارش', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}'

