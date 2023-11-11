# Generated by Django 4.2.6 on 2023-10-19 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('handelExcel', '0002_usedcar'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='category',
            field=models.CharField(choices=[('1', 'Category 1'), ('2', 'Category 2'), ('1A', 'Category 1A'), ('2A', 'Category 2A'), ('3A', 'Category 3A'), ('1B', 'Category 1B'), ('2B', 'Category 2B'), ('3B', 'Category 3B'), ('4B', 'Category 4B'), ('1C', 'Category 1C'), ('2C', 'Category 2C'), ('3C', 'Category 3C'), ('4C', 'Category 4C'), ('5C', 'Category 5C'), ('1D', 'Category 1D'), ('2D', 'Category 2D'), ('3D', 'Category 3D'), ('4D', 'Category 4D'), ('5D', 'Category 5D'), ('6D', 'Category 6D'), ('1E', 'Category 1E'), ('2E', 'Category 2E'), ('3E', 'Category 3E'), ('4E', 'Category 4E'), ('5E', 'Category 5E'), ('6E', 'Category 6E'), ('7E', 'Category 7E')], default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='make',
            field=models.CharField(choices=[('Hyundai', 'Hyundai'), ('Opel', 'Opel'), ('KIA', 'KIA'), ('DFSK', 'DFSK'), ('Fiat', 'Fiat'), ('Honda', 'Honda'), ('Chevorlet', 'Chevorlet'), ('Mini', 'Mini'), ('Toyota', 'Toyota'), ('Audi', 'Audi'), ('Nissan', 'Nissan'), ('DS', 'DS'), ('Renault', 'Renault'), ('Jaguar', 'Jaguar'), ('Mercedes', 'Mercedes'), ('Proton', 'Proton'), ('Mitsubishi', 'Mitsubishi'), ('BYD', 'BYD'), ('MG', 'MG'), ('Porsche', 'Porsche'), ('BMW', 'BMW'), ('Jetour', 'Jetour'), ('Scoda', 'Scoda'), ('Jeep', 'Jeep'), ('Lip Motor', 'Lip Motor'), ('Ford', 'Ford'), ('Land Rover', 'Land Rover'), ('Changan', 'Changan'), ('Mazda', 'Mazda'), ('Bestune', 'Bestune'), ('Subaro', 'Subaro'), ('Seyat', 'Seyat'), ('Jelly', 'Jelly'), ('Citroen', 'Citroen'), ('Dong Feng', 'Dong Feng'), ('KAIVI', 'KAIVI'), ('JAC', 'JAC'), ('Suzuki', 'Suzuki'), ('Lada', 'Lada'), ('Alfa Romeo', 'Alfa Romeo'), ('Peugeot', 'Peugeot'), ('Cupra', 'Cupra'), ('Volvo', 'Volvo'), ('Sang Yong', 'Sang Yong'), ('Cherry', 'Cherry'), ('Forthing', 'Forthing'), ('Volkswagen', 'Volkswagen'), ('Lexus', 'Lexus'), ('Aston Martin', 'Aston Martin'), ('Payek', 'Payek'), ('Haval', 'Haval'), ('Sawaist', 'Sawaist'), ('Massarati', 'Massarati')], max_length=100),
        ),
    ]
