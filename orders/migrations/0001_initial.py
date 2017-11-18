# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 23:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=250)),
                ('address2', models.CharField(blank=True, max_length=250, null=True)),
                ('address3', models.CharField(blank=True, max_length=250, null=True)),
                ('postal_code', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(choices=[('option 1', 'UK'), ('option 2', 'USA')], default='UK', max_length=10)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='ItemOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(db_index=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agree_terms', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('paid', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('sender_first_name', models.CharField(max_length=50)),
                ('sender_last_name', models.CharField(max_length=50)),
                ('sender_email', models.EmailField(max_length=254)),
                ('child_first_name', models.CharField(max_length=50)),
                ('child_last_name', models.CharField(max_length=50)),
                ('child_address', models.CharField(max_length=250)),
                ('child_address2', models.CharField(blank=True, max_length=250, null=True)),
                ('child_address3', models.CharField(blank=True, max_length=250, null=True)),
                ('child_postal_code', models.CharField(max_length=20)),
                ('child_city', models.CharField(max_length=100)),
                ('child_country', models.CharField(choices=[('UK', 'UK'), ('USA', 'USA')], default='UK', max_length=10)),
                ('child_boy_girl', models.CharField(choices=[('M', 'Boy'), ('F', 'Girl')], default='Boy', max_length=10)),
                ('child_age', models.IntegerField(blank=True, null=True)),
                ('child_birth_year', models.IntegerField(default=2013)),
                ('child_birth_month', models.CharField(choices=[('1', 'January'), ('2', 'February'), ('3', 'March'), ('4', 'April'), ('5', 'May'), ('6', 'June'), ('7', 'July'), ('8', 'August'), ('9', 'September'), ('10', 'October'), ('11', 'November'), ('12', 'December')], default=1, max_length=10)),
                ('child_birth_day', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('21', '21'), ('22', '22'), ('23', '23'), ('24', '24'), ('25', '25'), ('26', '26'), ('27', '27'), ('28', '28'), ('29', '29'), ('30', '30'), ('31', '31')], default=1, max_length=10)),
                ('child_age_time', models.CharField(choices=[('Years', 'Years'), ('Year', 'Year'), ('Month', 'Months'), ('Month', 'Month'), ('Days', 'Days')], default='Years', max_length=10)),
                ('child_relative_name', models.CharField(max_length=50)),
                ('child_friend_name', models.CharField(max_length=50)),
                ('child_present', models.CharField(max_length=200)),
                ('child_achievement', models.CharField(max_length=200)),
                ('letter_design', models.CharField(choices=[('1', 'letter1'), ('2', 'letter2'), ('3', 'letter3'), ('4', 'letter4'), ('5', 'letter5')], default='1', max_length=10)),
                ('pdf_download', models.BooleanField(default=False)),
                ('agree_terms', models.BooleanField(default=False)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orders.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='shop.Product')),
            ],
        ),
        migrations.AddField(
            model_name='itemoption',
            name='orderitem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_option_id', to='orders.OrderItem'),
        ),
        migrations.AddField(
            model_name='itemoption',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_option', to='shop.Product'),
        ),
        migrations.AddField(
            model_name='customer',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_order', to='orders.Order'),
        ),
    ]
