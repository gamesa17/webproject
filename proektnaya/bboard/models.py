from django.db import models


class BBoard(models.Model):
    title = models.CharField(max_length=50, verbose_name = "Предложение по разработке")
    content = models.TextField(null=True, blank=True, verbose_name = "Описание задачи")
    price = models.FloatField(null=True, blank=True, verbose_name = "Предлогаемая цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name = "Дата публикации")
    rubic = models.ForeignKey('Rubric', null = True, on_delete = models.PROTECT, verbose_name = "Рубрика")

    class Meta:
        verbose_name_plural = "Акутальные предложения"
        verbose_name = "Актуальное предложение"
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
#привет