# Generated by Django 3.2.12 on 2022-04-13 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("order", "0141_update_orderline_pk"),
        ("warehouse", "0023_alter_orderline_relations"),
    ]

    operations = [
        # for Allocation model
        migrations.AlterField(
            model_name="allocation",
            name="order_line_token",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="order.orderline"
            ),
        ),
        # migrations.AlterUniqueTogether(
        #     name='allocation',
        #     unique_together={('order_line_token', 'stock')},
        # ),
        migrations.RemoveField(
            model_name="allocation",
            name="order_line",
        ),
        migrations.RenameField(
            model_name="allocation",
            old_name="order_line_token",
            new_name="order_line",
        ),
        # migrations.AlterUniqueTogether(
        #     name='allocation',
        #     unique_together={('order_line', 'stock')},
        # ),
        migrations.AlterField(
            model_name="allocation",
            name="order_line",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="allocations",
                to="order.orderline",
            ),
        ),
        # for PreorderAllocation model
        migrations.AlterField(
            model_name="preorderallocation",
            name="order_line_token",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="order.orderline"
            ),
        ),
        # migrations.AlterUniqueTogether(
        #     name='preorderallocation',
        #     unique_together={('order_line_token', 'product_variant_channel_listing')},
        # ),
        migrations.RemoveField(
            model_name="preorderallocation",
            name="order_line",
        ),
        migrations.RenameField(
            model_name="preorderallocation",
            old_name="order_line_token",
            new_name="order_line",
        ),
        # migrations.AlterUniqueTogether(
        #     name='preorderallocation',
        #     unique_together={('order_line', 'product_variant_channel_listing')},
        # ),
        migrations.AlterField(
            model_name="preorderallocation",
            name="order_line",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="preorder_allocations",
                to="order.orderline",
            ),
        ),
    ]
