from django.test import TestCase
from librarian.models import Book,Student

class StudentTestCase(TestCase):
	def setUp(self):
		Student.objects.create(
			student_name = 'TestStudent1',
			student_id = '15011011C99999',
			student_class = 'TE',
			student_Div = 'A',
			student_email = 'testmail@mail.com',
			student_phno = 9898989898
		)
		
	def test_student_has_name(self):
		"""Checks if the student has a name"""
		test_student = Student.objects.get(student_id = '15011011C99999')
		self.assertEqual(str(test_student), test_student.student_name)
		
class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create(
			book_id = 101,
			title = 'TestBook1', 
			author = 'TestAuthor',
			publisher = 'TestPublisher',
			status = 'a'
		)
        Book.objects.create(
			book_id = 102,
			title = 'TestBook2', 
			author = 'TestAuthor',
			publisher = 'TestPublisher',
			status = 'a'
		)

    def test_books_have_title(self):
        """Books that have title have been created correctly"""
        test_book1 = Book.objects.get(title = 'TestBook1')
        test_book2 = Book.objects.get(title = 'TestBook2')
        self.assertEqual(str(test_book1), 'TestBook1')
        self.assertEqual(str(test_book2), 'TestBook0')