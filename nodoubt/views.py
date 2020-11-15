from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm, UserEditForm, StudentEditForm, QuestionForm
from django.contrib.auth.decorators import login_required
from .models import Student

# Create your views here.


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabled account')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'nodoubt/login.html', {'form': form})


@login_required
def dashboard(request):
    ques_form = QuestionForm()
    if request.method == 'POST':
        ques_form = QuestionForm(request.POST)
        if ques_form.is_valid():
            ques_form.save()
            return redirect('/')
    return render(request,
               'nodoubt/dashboard.html',
               #{'section': 'dashboard'},
               {'ques_form': ques_form}
               )


def	register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
               #	Create	a new user object	but	avoid	saving	it	yet
            new_user = user_form.save(commit=False)
            #	Set	the	chosen	password
            new_user.set_password(user_form.cleaned_data['password'])
            #	Save	the	User	object
            new_user.save()
            Student.objects.create(user=new_user)
            return render(request,
                       'account/register_done.html',
                       {'new_user':	new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request,
               'account/register.html',
               {'user_form': user_form})

