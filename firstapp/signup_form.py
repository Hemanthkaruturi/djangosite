from django import forms
from firstapp.models import Users

class NewUser(forms.ModelForm):
	class Meta:
		model = Users
		fields = '__all__'