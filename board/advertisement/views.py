from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


def advertisement_list(request):
    adv_list_1 = ['Мастер на час', 'Мастер на 2 часа', 'Мастер на 3 часа']
    adv_list_2 = ['Установка разеток', 'Замена лампочек', 'Установка выключателей']
    adv_list_3 = ['Установка раковины', 'Установка сифона', 'Установка полотенцесушителя']
    return render(
        request,
        'advertisement/advertisement_list.html',
        {'advertisements': [adv_list_1, adv_list_2, adv_list_3]})


def advertisement_details(request):
    return render(request, 'advertisement/advertisement_details.html', {})


def contacts(request):
    contacts = ['8-800-708-19-45', 'sales@company.com']
    return render(request, 'advertisement/contacts.html', {'contacts': contacts})


def about(request):
    about = ['Бесплатные объявления', 'Бесплатные объявления в вашем городе']
    return render(request, 'advertisement/about.html', {'about': about})


def categories(request):
    categories = ['Личные вещи', 'Транспорт', 'Хобби', 'Отдых']
    return render(request, 'advertisement/categories.html', {'categories': categories})


class RegionsView(View):
    def get(self, request):
        regions = ['Московская область', 'Татарстан', 'Кировская область', 'Краснодарский край']
        return render(request, 'advertisement/regions.html', {'regions': regions})

    def post(self, request):
        return render(request, 'advertisement/regions.html', {'regions': ['Регион успешно создан']})
