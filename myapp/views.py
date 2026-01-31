from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# READ
def item_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

# CREATE
def item_create(request):
    form = ItemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'form.html', {'form': form})

# UPDATE
def item_update(request, id):
    item = get_object_or_404(Item, id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('item_list')
    return render(request, 'form.html', {'form': form})

# DELETE
def item_delete(request, id):
    item = get_object_or_404(Item, id=id)
    item.delete()
    return redirect('item_list')
