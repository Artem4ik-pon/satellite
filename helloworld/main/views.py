from django.shortcuts import render
import requests
import pandas as pd
import matplotlib.pyplot as plt

def index(request):
    data = {
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', data)

def about(request):
    data_about = {
        'title': 'Про нас'
    }
    return render(request, 'main/about.html', data_about)


def contacts(request):
    data_contacts = {
        'title': 'Контакты',
        'objects': {
            'Сорочинский Артем - +7-***-***-83-52': 'Artyom',
            'Мельников Андрей - +7-***-***-81-58': 'Andrew',
            'Хайруллин Марат - +7-***-***-16-19': 'Marat',
            'Тайлаков Александр - +7-***-***-50-16': 'Alexandr',
            'Дуничев Николай - +7-***-***-**-**': 'Nikolay'
        }
    }
    return render(request, 'main/contacts.html', data_contacts)




def satellite_one(request):
    data_satellite = {
        'title': 'График наклона спутника',
        'dict': {
            'График наклона спутника KUZBASS-300'
        }
    }
    return render(request, 'main/satellite_one.html', data_satellite)


def satellite11(request):
    data_kuzbass1 = pd.Series(
        {"Декабрь": 94.5932, "Январь": 95.1193, "Февраль": 95.8412, "Март": 96.4876, "Апрель": 96.9965, "Май": 97.3799})
    plt.plot(data_kuzbass1, label='KUZBASS-300 (RS34S)')
    plt.legend()
    plt.xlabel('Месяц')
    plt.ylabel('Угол наклона')
    plt.title('Данные спутника KUZBASS-300')
    plt.show()
    return render(request, 'main/satellite_one.html')

def satellite12(request):
    data_kuzbass2 = pd.Series(
        {"Декабрь": 50725, "Январь": 51385, "Февраль": 51995, "Март": 52515, "Апрель": 53145, "Май": 53865})
    plt.plot(data_kuzbass2, label='KUZBASS-300 (RS34S)')
    plt.legend()
    plt.xlabel('Месяц')
    plt.ylabel('Эксцентриситет')
    plt.title('Данные спутника KUZBASS-300')
    plt.show()
    return render(request, 'main/satellite_one.html')


def satellite_two(request):
    data_satellite = {
        'title': 'График наклона спутника',
        'dict': {
            'График наклона спутника KUZGTU-1'
        }
    }
    return render(request, 'main/satellite_two.html', data_satellite)


def satellite21(request):
    data_kuzgtu1 = pd.Series(
        {"Декабрь": 45.2132, "Январь": 46.1254, "Февраль": 46.7898, "Март": 47.3658, "Апрель": 48.0121, "Май": 48.5698})
    plt.plot(data_kuzgtu1, label='KUZGTU-1')
    plt.legend()
    plt.xlabel('Месяц')
    plt.ylabel('Значение')
    plt.title('Данные спутника KUZGTU-1')
    plt.show()
    return render(request, 'main/satellite_two.html')

def satellite22(request):
    data_kuzgtu2 = pd.Series(
        {"Декабрь": 35565, "Январь": 36005, "Февраль": 36815, "Март": 37345, "Апрель": 37995, "Май": 38435})
    plt.plot(data_kuzgtu2, label='KUZGTU-1')
    plt.legend()
    plt.xlabel('Месяц')
    plt.ylabel('Значение')
    plt.title('Данные спутника KUZGTU-1')
    plt.show()
    return render(request, 'main/satellite_two.html')