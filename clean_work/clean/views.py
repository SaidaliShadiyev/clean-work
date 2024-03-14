from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import ContactForm

def base(request):
      return HttpResponse('')

def index(request):
      offers_list = Offers.objects.all()
      customer = Customers.objects.all()
      context = {'offers_list': offers_list, 'customer': customer,}
      return render(request, 'clean_work/index.html', context)

def service(request):
      services = Offers.objects.all()
      context = {'services': services,}
      return render(request, 'clean_work/service.html', context)

def service_detail(request, service_id):
      service = Offers.objects.get(pk=service_id)
      context = {'service': service,}
      return render(request, 'clean_work/service_detail.html', context)

def about_us(request):
      return render(request,'clean_work/about-us.html') 

def contact(request):
      if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                 return redirect('index')
      return render(request, 'clean_work/contact.html')


def policy(request):
      return render(request, 'clean_work/policy.html')
