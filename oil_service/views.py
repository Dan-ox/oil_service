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
    CarModelsModel
)


def client_view(request):
    clients = ClientsDataModel.objects.all()
    club_admins = ClubAdminsModel.objects.all()
    chronos = ChronosModel.objects.all()
    context = {'clients': clients, 'admins': club_admins, 'chronos': chronos}

    return render(request, 'oil_service/index.html', context=context)


def insert_data_view(request):
    if request.method == 'POST':
        if request.POST.get('first_name') and \
                request.POST.get('last_name') and \
                request.POST.get('phone_number') and \
                request.POST.get('email') and \
                request.POST.get('car_number') and \
                request.POST.get('city_name') and \
                request.POST.get('club_name') and \
                request.POST.get('phone_number') and \
                request.POST.get('phone_number') and \
                request.POST.get('phone_number'):
            table = ClientsTableModel()
            table.car_brand_name = request.POST.get('first_name')
            try:
                table.save()
                messages.success(request, 'Марка авто {} успешно сохранена'.format(table.car_brand_name))
            except IntegrityError:
                messages.error(request, '(!!!!!) МАРКА АВТО {} УЖЕ СУЩЕСТВУЕТ(!!!!!)'.format(table.car_brand_name))
            finally:
                return render(request, 'oil_service/insert.html')
    else:
        clubs = ClubsModel.objects.all()
        cities = CitiesModel.objects.all()
        car_brands = CarBrandsModel.objects.all()
        context = {'cities': cities, 'clubs': clubs, 'car_brands': car_brands}
        return render(request, 'oil_service/insert.html', context=context)


def admin_page_view(request):
    return render(request, 'oil_service/admin_page.html')
