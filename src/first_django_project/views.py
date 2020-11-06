from django.shortcuts import render
import datetime

def home(request):
    date = datetime.datetime.now().date()
    name = 'Kevin'
    _context_ = {'date': date, 'name': name}
