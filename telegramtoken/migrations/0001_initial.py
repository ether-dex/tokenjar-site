# Generated by Django 2.0.7 on 2018-07-23 11:08

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import telegramtoken.validators
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
                ('walletid', models.CharField(help_text='A valid blockchain wallet address.', max_length=60, verbose_name='Wallet-ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ActivationMode',
            fields=[
                ('ident', models.CharField(choices=[('PAYMENT', 'On-chain Payment'), ('TOKEN', 'On-chain Tokenization')], max_length=24, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'verbose_name_plural': 'Transaction Models',
                'verbose_name': 'Transaction Model',
            },
        ),
        migrations.CreateModel(
            name='TelegramContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ident', models.CharField(blank=True, max_length=55, verbose_name='ISCC')),
                ('title', models.CharField(max_length=128, verbose_name='Content Title')),
                ('extra', models.CharField(blank=True, default='', max_length=128, verbose_name='Extra Info')),
                ('file', models.FileField(help_text="Supported file types: ('jpg', 'png', 'txt', 'docx')", upload_to='mediafiles', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('jpg', 'png', 'txt', 'docx'))], verbose_name='Telegram Content File')),
                ('name', models.CharField(max_length=255, verbose_name='Filename')),
                ('tophash', models.CharField(blank=True, default='', max_length=64, verbose_name='tophash')),
                ('txid', models.CharField(blank=True, default='', help_text='Blockchain TX-ID of registered ISCC', max_length=64, verbose_name='Transaction-ID')),
            ],
            options={
                'verbose_name_plural': 'Telegram Contents',
                'verbose_name': 'Telegram Content',
            },
        ),
        migrations.CreateModel(
            name='TelegramToken',
            fields=[
                ('ident', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Identifier of this specific TelegramToken offer', primary_key=True, serialize=False, verbose_name='Telegram token ID')),
                ('info', models.CharField(help_text='A short public description about the Telegram token. Will also be added as info to tokens.', max_length=255, verbose_name='Public Info')),
                ('txid', models.CharField(blank=True, default='', help_text='Blockchain TX-ID of published Telegram token', max_length=64, verbose_name='Transaction-ID')),
                ('material', models.ForeignKey(help_text='The contract materials for this TelegramToken', on_delete=django.db.models.deletion.CASCADE, related_name='material_telegramtokens', to='telegramtoken.TelegramContent', verbose_name='Telegram Content')),
                ('transaction_model', models.ForeignKey(blank=True, help_text='Transaction Model accepted by the TelegramToken. If no Transaction Model is given the TelegramToken is purely informational and there is no defined way to close a license contract on-chain.', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='telegramtoken.ActivationMode', verbose_name='Transaction Model')),
            ],
            options={
                'verbose_name_plural': 'Telegram token',
                'verbose_name': 'Telegram token',
            },
        ),
        migrations.CreateModel(
            name='TelegramTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient', models.CharField(help_text='Walled-ID of user to whom you want to send the Telegram token Token', max_length=64, validators=[telegramtoken.validators.validate_address], verbose_name='Recipient')),
                ('txid', models.CharField(blank=True, default='', help_text='Blockchain TX-ID of token transaction', max_length=64, verbose_name='Transaction-ID')),
                ('telegram_token', models.ForeignKey(help_text='Choose Telegram token for which you want to send a Token', on_delete=django.db.models.deletion.CASCADE, to='telegramtoken.TelegramToken', verbose_name='Telegram token')),
            ],
            options={
                'verbose_name_plural': 'Token Transactions',
                'verbose_name': 'Token Transaction',
            },
        ),
    ]
