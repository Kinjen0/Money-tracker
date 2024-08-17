from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home(request):
    return render(request, 'Home.html')




@login_required
def Main_Screen(request):
    purchase_form = Purchase_Form()
    category_form = Category_Form()
    filter_form = Category_Filter_Form(user=request.user, data=request.GET)

    # Handle POST requests for new purchases or categories
    if request.method == 'POST':
        if 'purchase_form' in request.POST:
            purchase_form = Purchase_Form(request.POST)
            if purchase_form.is_valid():
                purchase = purchase_form.save(commit=False)
                purchase.user = request.user
                purchase.save()
                return redirect('purchases')

        elif 'category_form' in request.POST:
            category_form = Category_Form(request.POST)
            if category_form.is_valid():
                category = category_form.save(commit=False)
                category.user = request.user
                category.save()
                return redirect('purchases')

    # Filter purchases based on the selected category
    purchases = Purchase.objects.filter(user=request.user)
    if filter_form.is_valid() and filter_form.cleaned_data['category']:
        purchases = purchases.filter(category=filter_form.cleaned_data['category'])

    # Fetch categories for the user
    categories = Category.objects.filter(user=request.user)

    context = {
        'purchase_form': purchase_form,
        'category_form': category_form,
        'filter_form': filter_form,
        'purchases': purchases,
        'categories': categories,
    }

    return render(request, 'purchases_home.html', context)
