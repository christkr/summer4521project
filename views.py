from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Item
from .forms import ItemForm

def home(request):
    return render(request, 'groceries/home.html')

@login_required
def search_items(request):
    query = request.GET.get('q')
    items = Item.objects.filter(name__icontains=query) if query else Item.objects.all()
    return render(request, 'groceries/search_items.html', {'items': items})

@login_required
@permission_required('groceries.add_item', raise_exception=True)
def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search_items')
    else:
        form = ItemForm()
    return render(request, 'groceries/add_item.html', {'form': form})

@login_required
@permission_required('groceries.change_item', raise_exception=True)
def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('search_items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'groceries/edit_item.html', {'form': form})

@login_required
@permission_required('groceries.delete_item', raise_exception=True)
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('search_items')
    return render(request, 'groceries/delete_item.html', {'item': item})

def all_items(request):
    items = Item.objects.all()
    return render(request, 'groceries/all_items.html', {'items': items})