from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # Save the form to the database
            form.save()
            return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        # Update the form with the data from the request
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            # Save the form to the database
            form.save()
            return redirect('get_todo_list')
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    # Get the item from the database
    item = get_object_or_404(Item, id=item_id)
    # Toggle the done field
    item.done = not item.done
    # Save the item back to the database
    item.save()
    return redirect('get_todo_list')


def delete_item(request, item_id):
    # Get the item from the database
    item = get_object_or_404(Item, id=item_id)
    # Delete the item
    item.delete()
    return redirect('get_todo_list')
