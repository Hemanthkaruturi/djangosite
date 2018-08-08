from django.shortcuts import render
from firstapp.models import Topic, Webpage, AccessRecord, Users
from . import forms
from firstapp.forms import UserForm, UserProfileInfoForm
from firstapp.signup_form import NewUser
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
# Create your views here.

def index(request):
	my_dict = {'insert_me':"Hey hey this is awesome", 'number':100}
	return render(request,'first_app/index.html', context=my_dict)

def hello(request):
	my_dict = {'insert_me':"Hey hey this is from hello"}
	return render(request,'first_app/hello.html', context=my_dict)

def bye(request):
	my_dict = {'insert_me':"Hey hey this is from bye"}
	return render(request,'first_app/bye.html', context=my_dict)

def django(request):
	webpage_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_record': webpage_list}
	return render(request, 'first_app/django.html', context=date_dict)

def users(request):
	users_list = Users.objects.all()
	users_dict = {'users': users_list}
	return render(request, 'first_app/users.html', context=users_dict)

def form_name_view(request):
	form = forms.FormName()

	if request.method == 'POST':
		form = forms.FormName(request.POST)

	if form.is_valid():
		print("Validation success!")
		print("Name:" + form.cleaned_data['name'])


	return render(request, 'first_app/form.html', {'form':form})

def signup(request):

	form = NewUser()

	if request.method == "POST":
		form = NewUser(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)

		else:
			print("Form Invalid")



	return render(request, 'second_app/signup.html',{'form':form})

def other(request):
	return render(request, 'first_app/other.html')

def relative(request):
	return render(request,'first_app/relative_url.html')

def base(request):
	return render(request,'first_app/base.html')

def registration(request):
	registered = False
	form = UserForm()

	if request.method == "POST":
		form = UserForm(request.POST)
		profile_form = UserProfileInfoForm(request.POST)

		if form.is_valid() and profile_form.is_valid():
			user = form.save()
			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user

			if 'profile_pic' in request.FILES:
				profile.profile_pic = request.FILES['profile_pic']

			profile.save()

			registered = True
		else:
			print(form.errors, profile_form.errors)
	else:
		form = UserForm()
		profile_form = UserProfileInfoForm()


	return render(request, 'first_app/registration.html', {'user_form':form, 'profile_form':profile_form, 'registered':registered})

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('index'))

def special(request):
	return HttpResponse("You are Loggedin")

def user_login(request):

	if request.method=='POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))

			else:
				return HttpResponse("Account Not Active")
		else:
			print("Login failed")
			print("Username: {} and password {}".format(username, password) )
			return HttpResponse("Invalid Login")
	else:
		return render(request, 'first_app/login.html',{})

