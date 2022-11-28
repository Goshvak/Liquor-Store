from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm
from . import models

def home_view(request):
    return render(request, 'store/home.html')

def review_view(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("store:home"))
    else:
        form = ReviewForm
    return render(request, 'store/review.html', context={'form': form})

def products(request):
    items = models.ItemsModel.objects.all()
    item_list = {'items':items}
    return render(request, 'store/products.html', context=item_list)