from django.http import request
from django.shortcuts import render
from datetime import datetime


def home_view(request):
    date_today = datetime.now().date()
    page_year = date_today.year
    return render(request, 'main/home.html', {'date_today':date_today, 'page_year':page_year})