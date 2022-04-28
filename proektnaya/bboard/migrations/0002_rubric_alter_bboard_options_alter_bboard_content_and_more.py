# Generated by Django 4.0.4 on 2022-04-26 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=20, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='bboard',
            options={'ordering': ['-published'], 'verbose_name': 'Актуальное предложение', 'verbose_name_plural': 'Акутальные предложения'},
        ),
        migrations.AlterField(
            model_name='bboard',
            name='content',
            field=models.TextField(blank=True, null=True, verbose_name='Описание задачи'),
        ),
        migrations.AlterField(
            model_name='bboard',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='Предлогаемая цена'),
        ),
        migrations.AlterField(
            model_name='bboard',
            name='published',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='bboard',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Предложение по разработке'),
        ),
        migrations.AddField(
            model_name='bboard',
            name='rubic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bboard.rubric', verbose_name='Рубрика'),
        ),
    ]