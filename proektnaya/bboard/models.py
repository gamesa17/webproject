from django.db import models




class Request(models.Model):
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True)
    author_name = models.CharField("Автор заявки", max_length=50)
    response = models.BooleanField("Ответ на заявку", null=True)

    def __str__(self):
        return self.author_name


class Member(models.Model):
    member = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True)
    member_name = models.CharField("Имя участника", max_length=50)

    class Meta:
        verbose_name = "Участник"
        verbose_name_plural = "Участники"

    def __str__(self):
        return self.member_name


class BBoard(models.Model):
    title = models.CharField(max_length=50, verbose_name="Предложение по разработке")
    content = models.CharField(max_length=500, null=True, blank=True, verbose_name="Описание задачи")
    #price = models.FloatField(null=True, blank=True, verbose_name = "Предлогаемая цена")
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата публикации")
    #rubric = models.ForeignKey('Rubric', null = True, on_delete = models.PROTECT, verbose_name = "Заказчик")
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE, null=True)
    requests = models.ManyToManyField(Request, blank=True, null=True)
    members = models.ManyToManyField(Member, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Акутальные предложения"
        verbose_name = "Актуальное предложение"
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Заказчики'
        verbose_name = 'Заказчик'
        ordering = ['name']


