from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Task
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_http_methods


@require_http_methods(['GET', 'POST'])
def register(request):
    if request.method == 'POST':
        form = request.POST
        username = form['username']
        email = form['user-mail']
        password = form['user-pass']
        if User.objects.filter(email=email).exists():
            messages.error(request, 'A user with that email already exists.')
        else:
            if username == '':
                username = email # for User.objects.create_user() must have a username
            else:
                user_count = User.objects.count
                username = username + f"{user_count + 1}" # make username unique
            User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'Registration successful, please log in')
            return redirect('login')
    return render(request, 'register.html')


@require_http_methods(['GET', 'POST'])
def login_view(request):
    if request.method == 'POST':
        form = request.POST
        email = form['user-mail']
        password = form['user-pass']
        user_obj = User.objects.filter(email=email).first() # email is unique
        if user_obj and user_obj.check_password(password):
            login(request, user_obj)
            messages.success(request, 'Login success!')
            return redirect('task-list')  
        messages.warning(request, "Incorrect email address or password.")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
@require_http_methods(['GET'])
def task_list(request):
    if request.user.is_anonymous:
        return redirect('login')
    pending_tasks = Task.objects.filter(user=request.user, done=False)
    done_tasks = Task.objects.filter(user=request.user, done=True)
    return render(request, 'list_tasks.html', {'pending': pending_tasks, 'done': done_tasks})


@login_required
@require_http_methods(['GET'])
def task_view(request, pk):
    task = Task.objects.get(pk=pk)
    return render(request, 'view_task.html', {'task': task})

@login_required
@require_http_methods(['POST', 'GET'])
def task_create(request):
    if request.method == 'POST':
        form = request.POST
        title = form['title']
        description = form['description']
        # create new task and save
        new_task = Task.objects.create(user=request.user, title=title, description=description)
        new_task.save()
        return redirect('task-list')
    return render(request, 'create_task_form.html')


@login_required
@require_http_methods(['GET', 'POST'])
def task_update(request, pk: str):
    task = Task.objects.get(pk=pk, user=request.user)
    if request.method == 'POST':
        form = request.POST
        title = form['title']
        description = form['description']
        change_made = False # update task flag to update only when necessary
        if task.title != title:
           task.title = title
           change_made = True
        if task.description != description:
           task.description = description
           change_made = True
        if change_made:
           task.save()
        else:
            print('no changes detected')
        return redirect('task-list')
    return render(request, 'update_task_form.html', {'task': task})


@login_required
def task_delete(request, pk: str):
    """ Delete a task """
    task = Task.objects.get(pk=pk, user=request.user)
    if task:
        task.delete() # delete task
    return redirect('task-list')

@login_required
def task_mark_as_done(request, pk: str):
    task = Task.objects.get(pk=pk, user=request.user)
    if task:
        task.done = True
        task.save()
    return redirect('task-list')

@login_required
def task_undo(request, pk: str):
    task = Task.objects.get(pk=pk, user=request.user)
    if task:
        task.done = False
        task.save()
    return redirect('task-list')