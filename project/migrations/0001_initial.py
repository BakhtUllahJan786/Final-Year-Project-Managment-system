# Generated by Django 4.0 on 2022-10-02 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_no', models.CharField(max_length=50)),
                ('project_title', models.CharField(max_length=50)),
                ('created_at', models.DateField(blank=True, null=True)),
                ('student_1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student1', to='student.student')),
                ('student_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student2', to='student.student')),
                ('student_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student3', to='student.student')),
                ('superviser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]
