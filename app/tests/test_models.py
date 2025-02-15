import pytest
from django.contrib.auth import get_user_model
from app.models.book import Book
from app.models.borrow import Borrow

User = get_user_model()

@pytest.mark.django_db
def test_user_model():
    user = User.objects.create_user(username='testuser', password='secret', email='test@example.com')
    assert user.username == 'testuser'
    assert user.email == 'test@example.com'
    assert user.check_password('secret')

@pytest.mark.django_db
def test_book_model():
    # Assuming Book has a 'title' field and an 'is_borrowed' boolean field
    book = Book.objects.create(title='Test Book', is_borrowed=False)
    assert book.title == 'Test Book'
    assert book.is_borrowed is False

@pytest.mark.django_db
def test_borrow_model(django_user_model):
    user = django_user_model.objects.create_user(username='testuser', password='secret', email='test@example.com')
    book = Book.objects.create(title='Test Book', is_borrowed=False)
    borrow = Borrow.objects.create(user=user, book=book)
    borrow.save()
    assert borrow.user == user
    assert borrow.book == book
    # checking string representation; adjust the expected format if needed
    expected_str = f"Borrowed by {borrow.user} (ID: {borrow.id}, Created: {borrow.created_at})"
    assert str(borrow) == expected_str
