from django.shortcuts import render, get_object_or_404, redirect

from .models import Lists

from .forms import AddListForm, CreateUserForm

def index(request):
    lists = Lists.objects.all()
    
    return render(request, 'core/index.html', {
        'lists':lists,
    })

def done_view(request, list_id):
    list_object = get_object_or_404(Lists, pk=list_id)
    list_object.delete()
    return redirect('core:index')


def add_list(request):
    if request.method == 'POST':
        form = AddListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:index')
    else:
        form = AddListForm

    return render(request, 'core/create_list.html', {
        'form':form,
    })

def edit_list_view(request, list_id):
    target_list = get_object_or_404(Lists, pk=list_id)
    
    if request.method == 'POST':
        form = AddListForm(data=request.POST, files=request.FILES, instance=target_list)

        if form.is_valid():
            target_list.save()

            return redirect('core:index')
    else:
        form = AddListForm(instance=target_list)

    return render(request, 'core/edit.html', {
        'form': form
    })

def create_user_view(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    else:
        form = CreateUserForm()
    
    return render(request, 'core/create_user.html', {
        'form':form,
    })

