from django.db import models

from django.db import models

class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Tour(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Application(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    date_applied = models.DateField(auto_now_add=True)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f'Application #{self.pk} - {self.client} - {self.tour}'
