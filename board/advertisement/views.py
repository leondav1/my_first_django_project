import random

from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from .models import Advertisement, AdvertisementStatus, AdvertisementType


def advertisement_list(request):
    adv_list_1 = ['Мастер на час', 'Мастер на 2 часа', 'Мастер на 3 часа']
    adv_list_2 = ['Установка разеток', 'Замена лампочек', 'Установка выключателей']
    adv_list_3 = ['Установка раковины', 'Установка сифона', 'Установка полотенцесушителя']
    return render(
        request,
        'advertisement/advertisement_list.html',
        {'advertisements': [adv_list_1, adv_list_2, adv_list_3]})


def advertisement_details(request):
    advertisements = Advertisement.objects.all()
    advertisement = random.choice(advertisements)
    return render(request, 'advertisement/advertisement_details.html', {'advertisement': advertisement})


def contacts(request):
    contacts = ['8-800-708-19-45', 'sales@company.com']
    return render(request, 'advertisement/contacts.html', {'contacts': contacts})


class About(TemplateView):
    template_name = 'advertisement/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Бесплатные объявления в вашем городе'
        context['title'] = 'Бесплатные объявления'
        context['description'] = """
        С вопросом – «Куда подать объявление? – в Москве сталкивается практически каждый.
        Это не большая проблема, если речь идет, например, об одном объявлении.
        Другое дело, когда размещать их приходится регулярно и в большом количестве.
        Автоматизировать и упростить подачу объявлений поможет профессиональный сервис
        бесплатных объявлений, через который можно отправить информацию на все сайты одновременно.
        """
        return context


def categories(request):
    categories = ['Личные вещи', 'Транспорт', 'Хобби', 'Отдых']
    return render(request, 'advertisement/categories.html', {'categories': categories})


class RegionsView(View):
    def get(self, request):
        regions = ['Московская область', 'Татарстан', 'Кировская область', 'Краснодарский край']
        return render(request, 'advertisement/regions.html', {'regions': regions})

    def post(self, request):
        return render(request, 'advertisement/regions.html', {'regions': 'Регион успешно создан'})


class AddDb(View):
    def get(self, request):
        status = AdvertisementStatus.objects.get(id=1)
        type_all = AdvertisementType.objects.all()
        for num in range(3, 500001):
            title = f'Объявление_{num}'
            description = 'С другой стороны консультация с широким активом позволяет оценить значение позиций, ' \
                          'занимаемых участниками в отношении поставленных задач.'
            type = random.choice(type_all)
            data = Advertisement(title=title,
                                 description=description,
                                 status=status,
                                 type=type)
            data.save()
        return render(request, 'advertisement/add.html', {'regions': 'Данные успешно добавлены'})
