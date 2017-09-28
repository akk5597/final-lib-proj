from django.conf.urls import url
from . import views
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as librarian_views
from django.core.urlresolvers import reverse
from django.conf.urls import include

urlpatterns =[

	url(r'^$', librarian_views.home, name ='home'),
	url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
	url(r'^issuebook/$', librarian_views.issuebook, name='issuebook'),
	url(r'^issuebook_success/$', librarian_views.issuebook_success, name ='issuebook_success'),
	url(r'^books/$', librarian_views.index, name='index'),
    url(r'^books/(?P<book_id>[0-9]+)/$', librarian_views.detail, name='detail'),
	#url(r'^studentdetails/$', auth_views.login, {'template_name': 'studentdetails.html'}, name='studentdetails'),
	#url(r'^Students/$', librarian_views.StudentListView, name='StudentListView'),

	url(r'^addstudent/$', librarian_views.add_student, name='addstudent'),
	url(r'^addbook/$', librarian_views.addbook, name='addbook'),
	url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
	url(r'^signup/$', librarian_views.signup, name='signup'),
	url(r'^signup_success/$', librarian_views.signup_success, name ='signup_success'),
	url(r'^addbook_success/$', librarian_views.addbook_success, name ='addbook_success'),
	url(r'^addstudent_success/$', librarian_views.addstudent_success, name ='addstudent_success'),
    url(r'^Book_search/$', librarian_views.Book_search, name='Book_search'),

    url(r'^student_search/$', librarian_views.Student_search, name='Student_search'),
	url(r'^students/$', librarian_views.all_student, name='all_student'),
    url(r'^students/(?P<stud_id>[0-9]+)/$', librarian_views.stud_detail, name='stud_detail'),

    url(r'^borrowed-book/$', librarian_views.all_borrower, name='all_borrower'),
    url(r'^return_book/(?P<book_id>[0-9]+)/$', librarian_views.return_book, name='return_book'),
    url(r'^upload_pdfs/$', librarian_views.model_form_upload, name='model_form_upload'),
]
