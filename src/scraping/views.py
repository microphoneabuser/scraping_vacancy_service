from django.shortcuts import render
from .models import Vacancy
from .forms import SearchForm

def home_view(request):
    form = SearchForm()
    city = request.GET.get('city')
    language = request.GET.get('language')
    qs =[]
    if city or language:
        _filter = {}
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language
        qs = Vacancy.objects.filter(**_filter)
    return render(request, 'fdp/home.html', {'object_list': qs, 'form': form})