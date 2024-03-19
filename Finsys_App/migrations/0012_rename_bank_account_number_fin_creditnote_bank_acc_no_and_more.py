# Generated by Django 4.2.4 on 2024-03-14 06:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Finsys_App', '0011_rename_company_fin_creditnote_history_company_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='bank_account_number',
            new_name='bank_acc_no',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='customer_billing_address',
            new_name='billing_address',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='cheque_number',
            new_name='cheque_no',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='credit_note_date',
            new_name='creditnote_date',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='credit_note_number',
            new_name='creditnote_no',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='advanced_paid',
            new_name='grandtotal',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='customer_gst_number',
            new_name='gst_type',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='customer_gst_type',
            new_name='gstin',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='customer_place_of_supply',
            new_name='invoice_no',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='invoice_number',
            new_name='place_of_supply',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='grand_total',
            new_name='tax_amount',
        ),
        migrations.RenameField(
            model_name='fin_creditnote',
            old_name='upi_number',
            new_name='upi_no',
        ),
        migrations.RenameField(
            model_name='fin_creditnote_history',
            old_name='credit_note',
            new_name='CreditNote',
        ),
        migrations.RenameField(
            model_name='fin_creditnote_reference',
            old_name='reference_number',
            new_name='reference_no',
        ),
        migrations.RemoveField(
            model_name='fin_creditnote',
            name='description',
        ),
        migrations.RemoveField(
            model_name='fin_creditnote',
            name='document',
        ),
        migrations.RemoveField(
            model_name='fin_creditnote',
            name='tax_amount_igst',
        ),
        migrations.RemoveField(
            model_name='fin_creditnote_items',
            name='item',
        ),
        migrations.RemoveField(
            model_name='fin_creditnote_items',
            name='tax_rate',
        ),
        migrations.AddField(
            model_name='fin_creditnote',
            name='file',
            field=models.FileField(default=None, null=True, upload_to='credit_notes'),
        ),
        migrations.AddField(
            model_name='fin_creditnote',
            name='igst',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='fin_creditnote',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_creditnote',
            name='paid_off',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='fin_creditnote',
            name='reference_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='fin_creditnote_items',
            name='price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AddField(
            model_name='fin_creditnote_items',
            name='tax',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 14)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 14)),
        ),
        migrations.AlterField(
            model_name='fin_attendance_history',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 14)),
        ),
        migrations.AlterField(
            model_name='fin_creditnote',
            name='status',
            field=models.CharField(default='Draft', max_length=150),
        ),
        migrations.AlterField(
            model_name='fin_creditnote_history',
            name='action',
            field=models.CharField(blank=True, choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='fin_creditnote_items',
            name='discount',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='fin_creditnote_items',
            name='hsn',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fin_creditnote_items',
            name='quantity',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='fin_creditnote_items',
            name='total',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='holiday_comment',
            name='date',
            field=models.DateField(default=datetime.date(2024, 3, 14)),
        ),
        migrations.CreateModel(
            name='Fin_CreditNote_Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=500, null=True)),
                ('Company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_company_details')),
                ('CreditNote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Finsys_App.fin_creditnote')),
            ],
        ),
        migrations.AddField(
            model_name='fin_creditnote_items',
            name='Item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Finsys_App.fin_items'),
        ),
    ]
