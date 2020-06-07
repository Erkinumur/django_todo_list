from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, UpdateView, CreateView
from django.urls import reverse, reverse_lazy

from .models import Todo
from .forms import TodoForm, SignUpForm, AuthUserForm


class ShowTodoList(LoginRequiredMixin, View):
    def get(self, request):
        todo_list = Todo.objects.filter(user=request.user)
        update = False
        context = {
            'todo_list': todo_list,
            'form': TodoForm(),
            'update': update,
        }
        return render(request, 'main.html', context=context)
    
    def post(self, request):
        todo_list = Todo.objects.filter(user=request.user)
        form = TodoForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            # obj.todo = todo
            obj.save()
        return render(request, 'main.html', context={'todo_list': todo_list, 'form': TodoForm(), 'success': True})


# class TodoEditView(UpdateView):
#     model = Todo
#     template_name = 'edit_todo.html'
#     form_class = TodoForm
#     success_url = reverse_lazy('index_page')

#     def get_context_data(self, **kwargs):
#         kwargs['update'] = True
#         return super().get_context_data(**kwargs)

@login_required
def edit_todo(request, pk):
    todo_list = Todo.objects.filter(user=request.user)
    obj = Todo.objects.get(pk=pk)
    update = False
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            update = True
        return redirect(reverse('index_page'))

    context = {
        'todo_list': todo_list,
        'form': TodoForm(instance = Todo.objects.get(pk=pk)),
        'update': update,
        'pk': pk,
    }
    
    return render(request, 'edit_todo.html', context=context)


@login_required
def delete_todo(request, pk):
    obj = get_object_or_404(Todo, pk=pk)
    obj.delete()

    return redirect('index_page')


def complete_todo(request, pk):
    obj = get_object_or_404(Todo, pk=pk)
    obj.complete = True
    obj.save()

    return redirect('index_page')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index_page')
    
    form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})


class SignInView(LoginView):
    template_name = 'sign_in.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('index_page')


# class SignUpView(CreateView):
#     model = User
#     template_name = 'sign_up.html'
#     form_class = SignUpForm
#     success_url = reverse_lazy('index_page')

#     def form_valid(self, form):
#         form_valid = super().form_valid(form)
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]
#         aut_user = authenticate(username=username, password=password)
#         auth_login(self.request, aut_user)
#         return form_valid

    
    
    