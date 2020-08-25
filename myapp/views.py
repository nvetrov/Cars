# from django.shortcuts import render
# Create your views here.
from django.db.models import Q
from django.views.generic import TemplateView, ListView
import q
from myapp.models import Car


class CarListView(ListView):
    model = Car
    template_name = "car_list.html"


class CarsView(TemplateView):
    template_name = "inc_filter.html"

    def get_context_data(self, **kwargs):
        params = self.request.GET
        query = Q()
        for key, value in params.items():
            if value and key in vars(Car):
                query &= Q(**{key: value})
                q(query)
        return {"cars": Car.objects.filter(query)}
