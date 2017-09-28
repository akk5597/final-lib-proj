from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from phonenumber_field.modelfields import PhoneNumberField
from django.forms import ModelForm
from .models import Book,Student,Librarian,IssueData
from datetime import date,timedelta
class SignUpForm(UserCreationForm):
	librarian_name = forms.CharField(
		label='Librarian Name',
		max_length=50,
		help_text='Enter your full name'
	)
	
	def __init__(self, *args, **kwargs):
		super(UserCreationForm, self).__init__(*args, **kwargs)
		self.fields['username'].help_text = 'Please enter your Username <strong>Eg:gaikwadabhishek </strong>'

	class Meta:
		model = User
		fields = ('username', 'librarian_name' , 'password1', 'password2', )
		widgets = {
			'username': forms.TextInput(),
			'librarian_name':forms.TextInput(),
			'password1':forms.TextInput(),
			'password2':forms.TextInput()
		}

class AddStudentForm(forms.ModelForm):
	class Meta:
		model = Student
		exclude=()

class AddBookForm(forms.ModelForm):
	
	class Meta:
		model=Book
		exclude=()


class IssueBookForm(forms.ModelForm):
    book=forms.ModelChoiceField(queryset=Book.objects.filter(status='a'), 
    widget=forms.Select(), 
    empty_label=u"Select",
        )
    due_back=forms.DateField(initial=date.today()+timedelta(days=15))
    borrower=forms.ModelChoiceField(queryset=Student.objects.filter(), 
    widget=forms.Select(), 
    empty_label=u"Select",
        )
    class Meta:
        model = IssueData
        fields = ('book','due_back','borrower')

from .models import Document
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )