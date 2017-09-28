from .models import Book,Student,Librarian,IssueData
import django_filters

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = ['book_id','title', 'author', ]

class StudentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = ['student_id','student_name','student_class','student_Div' ,]