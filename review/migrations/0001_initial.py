# Generated by Django 4.2.4 on 2023-10-29 12:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book', '0002_auto_20231029_1255'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, null=True)),
                ('likes_count', models.IntegerField(default=False)),
                ('dislikes_count', models.IntegerField(default=False)),
                ('username', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, null=True)),
                ('review', models.TextField(max_length=1000, null=True)),
                ('rating', models.IntegerField(default=0, null=True, validators=[django.core.validators.MinValueValidator(0, message='Minimum rating is 0!'), django.core.validators.MaxValueValidator(100, message='Maximum rating is 100!')])),
                ('date_added', models.DateField(auto_now_add=True, null=True)),
                ('books', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book.book')),
            ],
            options={
                'ordering': ['-date_added'],
            },
        ),
    ]
