# Generated by Django 4.2.5 on 2023-09-29 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_plan', '0005_alter_dishtype_recipes_alter_foodlist_food_names_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='name',
            field=models.CharField(default='recipe_name', max_length=250, verbose_name='Название рецепта'),
            preserve_default=False,
        ),
    ]
