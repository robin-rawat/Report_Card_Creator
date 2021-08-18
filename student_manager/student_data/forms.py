from django import forms

class StudentInputForm(forms.Form):
	first_name = forms.CharField()
	last_name = forms.CharField()