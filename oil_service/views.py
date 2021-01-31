from django.shortcuts import render
from django.contrib import messages
from django.db.utils import IntegrityError

from .models import (
    ClientsDataModel,
    ClubAdminsModel,
    ChronosModel,
    CarBrandsModel,
    ClientsTableModel,
    CitiesModel,
    ClubsModel,
    CarModelsModel,
    DiscountsModel
)


def client_view(request):
    clients = ClientsDataModel.objects.all()
    club_admins = ClubAdminsModel.objects.all()
    chronos = ChronosModel.objects.all()
    context = {'clients': clients, 'admins': club_admins, 'chronos': chronos}

    return render(request, 'oil_service/index.html', context=context)


def insert_data_view(request):
    queryset_model = None
    if request.method == 'POST':
        if request.POST.get('first_name') and \
                request.POST.get('last_name') and \
                request.POST.get('phone_number') and \
                request.POST.get('email') and \
                request.POST.get('car_number') and \
                request.POST.get('city_name') and \
                request.POST.get('club') and \
                request.POST.get('car_brand_name') and \
                request.POST.get('car_model') and \
                request.POST.get('discount'):

            brand = request.POST.get('car_brand_name')
            model = request.POST.get('car_model')

            table = ClientsTableModel()
            table.first_name = request.POST.get('first_name')
            table.last_name = request.POST.get('last_name')
            table.phone_number = request.POST.get('phone_number')
            table.email = request.POST.get('email')
            table.car_number = request.POST.get('car_number')
            table.city = request.POST.get('city_name')
            table.club = request.POST.get('club')
            table.car_model = request.POST.get('car_model')
            table.discount = request.POST.get('discount')

            try:
                table.save()
                messages.success(request, 'Марка авто {} успешно сохранена'.format(table.first_name, table.last_name))
            except IntegrityError:
                messages.error(request, '(!!!!!) МАРКА АВТО {} УЖЕ СУЩЕСТВУЕТ(!!!!!)'.format(table.first_name,
                                                                                             table.last_name))
            finally:
                return render(request, 'oil_service/insert.html')
    else:
        clubs = ClubsModel.objects.all()
        cities = CitiesModel.objects.all()
        car_models = CarModelsModel.objects.all()
        car_brands = CarBrandsModel.objects.all()
        discounts = DiscountsModel.objects.all()
        context = {'cities': cities, 'clubs': clubs, 'car_brands': car_brands, 'car_models': car_models,
                   'discounts': discounts}
        return render(request, 'oil_service/insert.html', context=context)


def admin_page_view(request):
    return render(request, 'oil_service/admin_page.html')
