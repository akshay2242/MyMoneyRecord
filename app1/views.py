from django.contrib.auth import authenticate, login
from django.http import request
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.base import TemplateView
from .models import Record
from .forms import RecordForm,CreateUserForm, LoginForm
from django.contrib.auth.views import  LogoutView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from app1 import forms

# Create your views here.
@method_decorator(staff_member_required, name='dispatch')
class CreateUser(CreateView):
    form_class = CreateUserForm
    template_name = 'app1/create_user.html'
    success_url = '/admin_dashboard/'

@method_decorator(login_required, name='dispatch')
class CreateRecord(CreateView):
    form_class = RecordForm
    template_name = 'app1/create_record.html'
    success_url = '/dashboard/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid:
            fm = form.save(commit=False)
            fm.user_id = self.request.user
            fm.save()
        return redirect('/user_dashboard/')

@method_decorator(login_required, name='dispatch')
class UpdateRecord(UpdateView):
    model = Record
    fields = ['name', 'date', 'amount', 'reason', 'status']
    template_name = 'app1/update_record.html'
    success_url = '/user_dashboard/'

def adminLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/admin_dashboard/')
        else:
            form = LoginForm()
        return render(request, 'app1/admin_login.html', {'form':form})
    else:
        return HttpResponseRedirect('/admin_dashboard/')

def userLogin(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect('/user_dashboard/')
        else:
            form = LoginForm()
        return render(request, 'app1/user_login.html', {'form':form})
    else:
        return HttpResponseRedirect('/user_dashboard/')

@method_decorator(login_required, name='dispatch')
class UserDashboard(TemplateView):
    def get(self, request, *args, **kwargs):
        data = Record.objects.all()
        user = self.request.user
        return render(request, 'app1/user_dashboard.html', {'user':user, 'data':data})


@method_decorator(staff_member_required, name='dispatch')
class AdmindDasboard(ListView):
    model = User
    context_object_name = 'data'
    template_name = 'app1/admin_dashboard.html'

class Logout(LogoutView):
    template_name = 'app1/logout.html'
