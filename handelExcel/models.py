from django.db import models

# Create your models here.
# models.py
from django.db import models
from handelExcel.utils import model_deduction_percentage,category_deduction_percentage,make_deduction_percentage
class Car(models.Model):
    
    CATEGORY_CHOICES = [
        ('1', 'Category 1'),
        ('2', 'Category 2'),
        ('1A', 'Category 1A'), ('2A', 'Category 2A'), ('3A', 'Category 3A'),
        ('1B', 'Category 1B'), ('2B', 'Category 2B'), ('3B', 'Category 3B'), ('4B', 'Category 4B'),
        ('1C', 'Category 1C'), ('2C', 'Category 2C'), ('3C', 'Category 3C'), ('4C', 'Category 4C'), ('5C', 'Category 5C'),
        ('1D', 'Category 1D'), ('2D', 'Category 2D'), ('3D', 'Category 3D'), ('4D', 'Category 4D'), ('5D', 'Category 5D'), ('6D', 'Category 6D'),
        ('1E', 'Category 1E'), ('2E', 'Category 2E'), ('3E', 'Category 3E'), ('4E', 'Category 4E'), ('5E', 'Category 5E'), ('6E', 'Category 6E'), ('7E', 'Category 7E'),
        # Add more choices as needed
    ]
    
    MAKE_CHOICES = [
        ('Hyundai', 'Hyundai'), ('Opel', 'Opel'), ('KIA', 'KIA'), ('DFSK', 'DFSK'),
        ('Fiat', 'Fiat'), ('Honda', 'Honda'), ('Chevorlet', 'Chevorlet'), ('Mini', 'Mini'),
        ('Toyota', 'Toyota'), ('Audi', 'Audi'), ('Nissan', 'Nissan'), ('DS', 'DS'),
        ('Renault', 'Renault'), ('Jaguar', 'Jaguar'), ('Mercedes', 'Mercedes'),
        ('Proton', 'Proton'), ('Mitsubishi', 'Mitsubishi'), ('BYD', 'BYD'), ('MG', 'MG'),
        ('Porsche', 'Porsche'), ('BMW', 'BMW'), ('Jetour', 'Jetour'), ('Scoda', 'Scoda'),
        ('Jeep', 'Jeep'), ('Lip Motor', 'Lip Motor'), ('Ford', 'Ford'),
        ('Land Rover', 'Land Rover'), ('Changan', 'Changan'), ('Mazda', 'Mazda'),
        ('Bestune', 'Bestune'), ('Subaro', 'Subaro'), ('Seyat', 'Seyat'), ('Jelly', 'Jelly'),
        ('Citroen', 'Citroen'), ('Dong Feng', 'Dong Feng'), ('KAIVI', 'KAIVI'),
        ('JAC', 'JAC'), ('Suzuki', 'Suzuki'), ('Lada', 'Lada'), ('Alfa Romeo', 'Alfa Romeo'),
        ('Peugeot', 'Peugeot'), ('Cupra', 'Cupra'), ('Volvo', 'Volvo'), ('Sang Yong', 'Sang Yong'),
        ('Cherry', 'Cherry'), ('Forthing', 'Forthing'), ('Volkswagen', 'Volkswagen'),
        ('Lexus', 'Lexus'), ('Aston Martin', 'Aston Martin'), ('Payek', 'Payek'),
        ('Haval', 'Haval'), ('Sawaist', 'Sawaist'), ('Massarati', 'Massarati'),
    ]
    make = models.CharField(max_length=100, choices=MAKE_CHOICES)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.IntegerField()
    location = models.CharField(max_length=100,null=False,blank=False)
    car_class = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    link = models.URLField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)
    def __str__(self):
        return f'{self.year} {self.make} {self.model}'







class UsedCar(models.Model):
    MODEL_CHOICES = [(str(key), str(key)) for key in model_deduction_percentage.keys()]
    CATEGORY_CHOICES = [(str(key), str(key)) for key in category_deduction_percentage.keys()]
    MAKE_CHOICES = [(str(key), str(key)) for key in make_deduction_percentage.keys()]
    YEAR_CHOICES = [(year, str(year)) for year in range(1970, 2023)]
    make = models.CharField(max_length=100, choices=MAKE_CHOICES)
    model = models.CharField(max_length=100, choices=MODEL_CHOICES)
    year = models.IntegerField(choices=YEAR_CHOICES, null=True, blank=True)
    color = models.CharField(max_length=50,null=True,blank=True)
    mileage = models.IntegerField()
    location = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)


    def __str__(self):
            return f'{self.year} {self.make} {self.model}'
        
        
    @classmethod
    def get_all_usedCars(cls):
        return cls.objects.all()    