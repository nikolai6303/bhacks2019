from django import forms
from .models import newuser,problems,reply,course,lectures
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class UserCreationForm(forms.ModelForm):
	password=forms.CharField(widget=forms.PasswordInput)
	class Meta:
		model=User
		fields=('username','email','password')
	def clean_password2(self):
		raise forms.ValidationError('password donot match')
		if 'password1' in self.cleaned_data:
			password1=self.cleaned_data['password1']
			password2=self.cleaned_data['password2']
			if password1==password2:
				return password2
		raise forms.ValidationError('password donot match')

class ProfileForm(forms.ModelForm):
	class Meta:
		model=newuser
		fields=('photo','mentor',)
class chat(forms.Form):
	prob=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))

class replyform(forms.Form):
	answer=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','class':'col-lg-6'}))

class AddCourses(forms.ModelForm):
	class Meta:
		model=course
		fields=('teacher','price','name','logo','description')
class AddLecture(forms.Form):
	video=forms.FileField()
	name=forms.CharField(max_length=100)

class paragraph(forms.Form):
	start=forms.CharField(max_length=100)
	new=forms.CharField(widget=forms.Textarea())

