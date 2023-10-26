# Generated by Django 4.2.6 on 2023-10-26 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("borrowings", "0003_rename_book_id_borrowing_book_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Payment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "status_payment",
                    models.CharField(
                        choices=[("PEN", "PENDING"), ("PAI", "PAID")], max_length=7
                    ),
                ),
                (
                    "type_payment",
                    models.CharField(
                        choices=[("PAY", "PAYMENT"), ("FIN", "FINE")], max_length=7
                    ),
                ),
                ("session_url", models.URLField()),
                ("session_id", models.CharField(max_length=255)),
                ("money", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "borrowing",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="borrowings.borrowing",
                    ),
                ),
            ],
        ),
    ]
