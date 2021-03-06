# Generated by Django 4.0.5 on 2022-07-03 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nabberapi', '0003_rename_user_description_user_user_fname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nabberapi.picture'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='nabberapi.picture'),
        ),
    ]
