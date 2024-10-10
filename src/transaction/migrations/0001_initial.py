# Generated by Django 5.1.1 on 2024-10-09 19:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owner', '0001_initial'),
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlanModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('name', models.CharField(max_length=180, verbose_name='Nom ')),
                ('description', models.TextField(verbose_name='Description ')),
                ('price', models.IntegerField(verbose_name='Prix ')),
            ],
            options={
                'verbose_name': "Plan d'abonnement",
                'verbose_name_plural': "Plan d'abonnements",
            },
        ),
        migrations.CreateModel(
            name='PaymentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('payment_type', models.CharField(choices=[('Abonnement', 'Abonnement'), ('Paiment de loyer', 'Paiment de loyer')], default='Abonnement', max_length=20, verbose_name='Type de paiement ')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_owner_id', to='owner.ownermodel')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payment_tenant_id', to='tenant.tenantmodel')),
            ],
            options={
                'verbose_name': 'Paiement',
                'verbose_name_plural': 'Paiements',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('ended', models.DateTimeField(verbose_name="Date de fin d'abonnement ")),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.ownermodel')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenant.tenantmodel')),
                ('subscription_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.subscriptionplanmodel')),
            ],
            options={
                'verbose_name': 'Abonnement',
                'verbose_name_plural': 'Abonnements',
            },
        ),
        migrations.CreateModel(
            name='HistoricModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='owner.ownermodel')),
                ('tenant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenant.tenantmodel')),
                ('subscription_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.subscriptionplanmodel')),
            ],
            options={
                'verbose_name': 'Historique',
                'verbose_name_plural': 'Historiques',
            },
        ),
    ]
