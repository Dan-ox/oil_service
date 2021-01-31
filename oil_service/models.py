from django.db import models


class ClientsDataModel(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    car_number = models.CharField(max_length=10)
    club_name = models.CharField(max_length=50)
    car_brand_name = models.CharField(max_length=50)
    model = models.CharField(max_length=70)
    discount = models.IntegerField()
    city_name = models.CharField(max_length=30)

    class Meta:
        db_table = u'"oil\".\"clients_data"'


class ClubAdminsModel(models.Model):
    club_name = models.CharField(max_length=50)
    admin_name = models.CharField(max_length=20)
    admin_last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)

    class Meta:
        db_table = u'"oil\".\"club_admins"'


class ChronosModel(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    service_date = models.DateField()
    service_type = models.CharField(max_length=100)
    discount = models.IntegerField()
    s_center_name = models.CharField(max_length=100)
    car_number = models.CharField(max_length=10)
    car_brand_name = models.CharField(max_length=50)
    model = models.CharField(max_length=70)

    class Meta:
        db_table = u'"oil\".\"chrono_data"'


# MODELS FOR TEMPLATE FORMS

class ClientsTableModel(models.Model):

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    car_number = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    club = models.IntegerField()
    car_model = models.IntegerField()
    # car_brand_name = models.CharField(max_length=50)
    discount = models.IntegerField()

    class Meta:
        db_table = u'"oil\".\"clients"'


class CitiesModel(models.Model):
    city_name = models.CharField(max_length=30)

    class Meta:
        db_table = u'"oil\".\"cities"'


class ClubsModel(models.Model):
    club_name = models.CharField(max_length=50)
    admin = models.IntegerField()

    class Meta:
        db_table = u'"oil\".\"clubs"'


class CarModelsModel(models.Model):
    brand = models.IntegerField()
    model = models.CharField(max_length=70)

    class Meta:
        db_table = u'"oil\".\"car_models"'


class CarBrandsModel(models.Model):
    car_brand_name = models.CharField(max_length=50)

    class Meta:
        db_table = u'"oil\".\"car_brands"'


class DiscountsModel(models.Model):
    amount = models.IntegerField()

    class Meta:
        db_table = u'"oil\".\"discounts"'
