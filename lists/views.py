from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from lists.models import Item


# TODO: Support more than 1 list
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
