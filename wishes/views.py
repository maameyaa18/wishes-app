from django.shortcuts import render, redirect
from .filters import WishFilter
from .forms import WishForm
from .models import Wishes

# Create your views here.
def index(request):
    return render(request, 'wishes/index.html')

def all_wishes(request):
    all_wishes = Wishes.objects.order_by('-list_date')
    my_Filter = WishFilter(request.GET, queryset=all_wishes)
    all_wishes = my_Filter.qs

    context = {'all_wishes': all_wishes, 'my_Filter': my_Filter}
    return render (request, 'wishes/all_wishes.html', context)

def new_wish(request):
    if request.method != 'POST':
        form = WishForm()
    else:
        form = WishForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('wishes:my_wishes')
      
    context = {'form': form}
    return render(request, 'wishes/new_wish.html', context)

def detail(request, detail_id):
    detail = Wishes.objects.get(id=detail_id)
    context = {'detail': detail}
    return render(request, 'wishes/detail.html', context)

def my_wishes(request):
    my_wishes = request.user.wishes_set.order_by('-list_date')
    context = {'my_wishes': my_wishes}
    return render (request, 'wishes/my_wishes.html', context)

def edit_wish(request, edit_id):
    wish = Wishes.objects.get(id=edit_id)
  
    if request.method != 'POST':
        form = WishForm(instance=wish)
    else:
        form = WishForm(request.POST, request.FILES, instance=wish)
        if form.is_valid():
            form.save()
            return redirect('wishes:all_wishes')

    context = {'wish': wish, 'form': form}
    return render(request, 'wishes/edit_wish.html', context)

def delete_wish(request, delete_id):
    wish = Wishes.objects.get(id=delete_id)
    if request.method == 'POST':
        wish.delete()
        return redirect('wishes:my_wishes')
    context = {'wish': wish}
    return render(request, 'wishes/delete_wish.html', context)