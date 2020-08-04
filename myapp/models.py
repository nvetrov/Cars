# TODO Ваше ТЗ
#  Весь проект Django состоит из одного приложения.
#  Необходимо описать модель автомобиля (Car) с полями:
#  производитель (BMW, Audi, Tesla и т.д.) (CharField)
#  модель авто (S, TT, X6 и т.д.) (CharField)
#  год выпуска (IntegerField) коробка передач (SmallIntegerField with choices "механика", "автомат", "робот") цвет
#  Необходимо создать главную страницу со списком автомобилей.
#  На главной странице создать форму «фильтрации» (поиска) автомобилей.
#  GET-запросом отправлять данные о фильтрах.
#  Во view собирать запрос с помощью Q-объектов и отображать авто на главной с учётом фильтров.


from django.db import models
# from django.contrib.auth import get_user_model
# User = get_user_model()


# Create your models here.
class Car(models.Model):
    MECHANIC, AUTO, ROBOT = range(3)
    KPP_CHOICES = [
        [MECHANIC, "Механическая коробка передач"],
        [AUTO, "Автоматическая коробка передач"],
        [ROBOT, "Роботизированная коробка передач"],
    ]
    manufacturer = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    kpp = models.SmallIntegerField(choices=KPP_CHOICES)
    color = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.manufacturer}, {self.model}, {self.year}, {self.kpp}, {self.color}'
