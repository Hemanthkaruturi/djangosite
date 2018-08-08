from django import forms
from django.core import validators
from django.contrib.auth.models import User
from firstapp.models import UserProfileInfo

class FormName(forms.Form):

	name = forms.CharField()
	email = forms.EmailField()
	verify_email = forms.EmailField(label='re-enter email')
	text = forms.CharField(widget = forms.Textarea)

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vemail = all_clean_data['verify_email']

		if email != vemail:
			raise forms.ValidationError("Make sure emails are same")


class UserForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
	class Meta:
		model = UserProfileInfo
		fields = ('portfolio_site','profile_pic')