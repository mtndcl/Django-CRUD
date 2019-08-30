from django import forms
from .models import User ,Profile,Post
from django.contrib.auth.forms import UserCreationForm

import datetime

from bootstrap_datepicker_plus import DatePickerInput
class MyDatePickerInput(DatePickerInput):
    template_name = 'User/updateprofile.html'
class registerform(UserCreationForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2','first_name','last_name']

	
	def clean_first_name(self,*args,**kwargs):
		first_name = self.cleaned_data.get('first_name')
		   
		print('ValidationError   func worked')
		if  len(first_name)<3:
			raise forms.ValidationError("At least 4 character need")
		else:
			return first_name
	def clean_last_name(self,*args,**kwargs):
		last_name = self.cleaned_data.get('last_name')
		   
		print('ValidationError   func worked')
		if  len(last_name)<3:
			raise forms.ValidationError("At least 4 character need")
		else:
			return last_name


class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email','last_name','first_name']


class ProfileUpdateForm(forms.ModelForm):

	
	birth_date = forms.DateField(
        input_formats=['%Y-%m-%d'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
	
	class Meta:
		model = Profile
		fields = ['bio', 'location', 'birth_date','image']

		

class Postform(forms.ModelForm):
	

	class Meta:
		model=Post
		fields = ['posttext']
	
	
		