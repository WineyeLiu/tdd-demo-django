from django.shortcuts import render, redirect
from lists.models import Item

# Create your views here.
def home_page(request):
    # print('------------', request.POST.get('item_text', ''))
    '''
    item = Item()
    item.text = request.POST.get('item_text', '')
    item.save()
    '''
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})

def view_list(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items':items})
