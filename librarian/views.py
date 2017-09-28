from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.conf.urls import include
from django.template import loader
from .models import Student
from django.http import Http404
from .forms import SignUpForm,AddStudentForm,AddBookForm,IssueBookForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from .models import Book,Student,Librarian,IssueData
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
# Create your views here.
from django.views import generic
@login_required
def home(request):
    return render(request, 'home.html')

def signup_success(request):
    return render(request,'signup_success.html')
@login_required
def addbook_success(request):
    return render(request,'addbook_success.html')

def addstudent_success(request):
    return render(request,'addstudent_success.html')

def issuebook_success(request):
	return render(request,'issuebook_success.html')

def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.refresh_from_db()
			user.student.librarian_name = form.cleaned_data.get('librarian_name')
			#user.student.email = form.cleaned_data.get('email')
			#user.student.phone_number = form.cleaned_data.get('phone_number')
			user.refresh_from_db()
			user.save()
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=user.username, password=raw_password)
			login(request, user)
			return redirect('signup_success')
	else:
		form = SignUpForm()
	return render(request, 'signup.html', {'form': form})
@login_required
def addbook(request):
	form = AddBookForm()
	if request.method=='POST':
		form = AddBookForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			form.save()
			return redirect('addbook_success')
		else:
			form = AddBookForm()
	return render(request,'addbook.html',{'form':form})

@login_required
def add_student(request):
	form = AddStudentForm()
	if request.method=='POST':
		form = AddStudentForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			form.save()
			return redirect('addstudent_success')
		else:
			form = AddStudentForm()
	return render(request,'addstudent.html',{'form':form})


from .filters import BookFilter,StudentFilter

def Book_search(request):
    book_list = Book.objects.all()
    Book_filter = BookFilter(request.GET, queryset=book_list)
    return render(request, 'librarian/Book_list_search.html', {'filter': Book_filter})

def all_student(request):
	all_stud = list(Student.objects.all())
	return render(request,'all_student.html',{'all_stud':all_stud})

def stud_detail(request, stud_id):
    user = request.user
    stud = get_object_or_404(Student, pk=stud_id)
    return render(request, 'stud-detail.html', {'stud': stud})

def Student_search(request):
    Student_list = Student.objects.all()
    Student_filter = StudentFilter(request.GET, queryset=Student_list)
    return render(request, 'librarian/Student_list_search.html', {'filter': Student_filter})

@login_required
def issuebook(request):
	form = IssueBookForm()
	if request.method=='POST':
		form = IssueBookForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			book = cd.get('book')
			borrower = cd.get('borrower')
			book.status = 'o'
			book.student_issued = borrower
			#print(book.student_issued.student_name)
			book.save()
			form.save()
			return redirect('issuebook_success')
		else:
			form = IssueBookForm()
			
	return render(request,'issuebook.html',{'form':form})

def detail(request, book_id):
    user = request.user
    _book = get_object_or_404(Book, pk=book_id)
    borrower=None
    if(_book.status=='o'):
    	Issued_book=list(IssueData.objects.all())
    	for i in Issued_book:
    		if(i.book.book_id==_book.book_id):
    			borrower=i.borrower

    return render(request, 'book-detail.html', {'book': _book,'borrower':borrower})

def index(request):
	all_book = list(Book.objects.all())
	print(all_book)
	return render(request,'index.html',{'all_book':all_book})
@login_required
def all_borrower(request):
	all_borrower=list(IssueData.objects.all())
	return render(request,'librarian/all_borrower.html',{'all_borrower':all_borrower})


from datetime import date,timedelta
from django.contrib import messages
@login_required
def return_book(request, book_id):
    """
    View responsible for marking that specific book has been returned to library.
   """
    _book = get_object_or_404(Book, pk=book_id)
    Issued_book=list(IssueData.objects.all())
    Book_2_return=IssueData.objects.all()
    for i in Issued_book:
    	if(i.book.book_id==book_id):
    		Book_2_return=i
    if _book.status=='o':
    	Book_2_return.borrower.fine=abs((date.today()- Book_2_return.due_back).days)
    	Book_2_return.borrower = None
    	_book.status = 'a'
    	Book_2_return.delete()
    	_book.save()
    	messages.success(request, _book.title[:] + ' has been marked as returned')
    	return detail(request, book_id)
    else:
    	return redirect('home')



from .forms import DocumentForm
def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'model_form_upload.html', {
        'form': form
    })    	