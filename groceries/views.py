from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Item
from .forms import ItemForm
from django.db import connections

def get_db_connection(user):
    if user.groups.filter(name='dbadmin').exists():
        return 'dbadmin'
    elif user.groups.filter(name='manager').exists():
        return 'manager'
    elif user.groups.filter(name='employee').exists():
        return 'employee'
    return 'default'

def home(request):
    return render(request, 'groceries/home.html')

@login_required
def search_items(request):
    db_conn = get_db_connection(request.user)
    query = request.GET.get('q')
    if query:
        items = Item.objects.using(db_conn).filter(name__icontains=query)
    else:
        items = Item.objects.using(db_conn).all()
    return render(request, 'groceries/search_items.html', {'items': items})

@login_required
@permission_required('groceries.add_item', raise_exception=True)
def add_item(request):
    db_conn = get_db_connection(request.user)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save(using=db_conn)
            return redirect('search_items')
    else:
        form = ItemForm()
    return render(request, 'groceries/add_item.html', {'form': form})

@login_required
@permission_required('groceries.change_item', raise_exception=True)
def edit_item(request, item_id):
    db_conn = get_db_connection(request.user)
    item = get_object_or_404(Item.objects.using(db_conn), id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save(using=db_conn)
            return redirect('search_items')
    else:
        form = ItemForm(instance=item)
    return render(request, 'groceries/edit_item.html', {'form': form})

@login_required
@permission_required('groceries.delete_item', raise_exception=True)
def delete_item(request, item_id):
    db_conn = get_db_connection(request.user)
    item = get_object_or_404(Item.objects.using(db_conn), id=item_id)
    if request.method == 'POST':
        item.delete(using=db_conn)
        return redirect('search_items')
    return render(request, 'groceries/delete_item.html', {'item': item})

def all_items(request):
    items = Item.objects.all()
    return render(request, 'groceries/all_items.html', {'items': items})