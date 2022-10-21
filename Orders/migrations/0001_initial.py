# Generated by Django 4.0.8 on 2022-10-21 10:11

from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UUID', shortuuid.django_fields.ShortUUIDField(alphabet='0123456789', auto_created=True, editable=False, length=10, max_length=10, prefix='', unique=True, verbose_name='UUID заказа')),
                ('user_id', models.PositiveIntegerField(editable=False)),
                ('product_info', models.TextField(blank=True, null=True, verbose_name='Список товаров')),
                ('adress', models.TextField(blank=True, null=True, verbose_name='Адрес клиента')),
                ('contacts', models.TextField(blank=True, null=True, verbose_name='Контакты клиента')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')),
                ('cart', models.JSONField(editable=False)),
                ('status', models.TextField(choices=[('CREATED', 'Платеж создан'), ('WAITING', 'Платёж в обработке / ожидает оплаты'), ('PAID', 'Платёж оплачен'), ('EXPIRED', 'Время жизни счета истекло. Счет не оплачен.'), ('REJECTED', 'Платёж отклонен')], default='CREATED', verbose_name='Статус заказа')),
            ],
            options={
                'verbose_name': 'текущий заказ',
                'verbose_name_plural': 'Текущие заказы',
                'ordering': ('-created',),
            },
        ),
    ]
