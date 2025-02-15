import pytest
from django.urls import reverse
from django.contrib.auth import get_user_model
from ..models import Book
from ..models import Borrow

User = get_user_model()

@pytest.mark.django_db
def test_signup_view(client):
    url = reverse('signup_view')
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_signup(client):
    url = reverse('signup')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'secret'
    }
    response = client.post(url, data)
    # Assuming successful signup redirects to login_view:
    assert response.status_code == 302
    assert User.objects.filter(username='testuser').exists()

@pytest.mark.django_db
def test_login(client, django_user_model):
    # create user
    user = django_user_model.objects.create_user(username='testuser', password='secret')
    url = reverse('login')
    data = {
        'username': 'testuser',
        'password': 'secret'
    }
    response = client.post(url, data)
    # Successful login redirects to profile
    assert response.status_code == 302

@pytest.mark.django_db
def test_profile_view(client, django_user_model):
    # create a user and log in
    user = django_user_model.objects.create_user(username='testuser', password='secret', email='test@example.com')
    client.login(username='testuser', password='secret')
    url = reverse('profile', kwargs={'username': 'testuser'})
    response = client.get(url)
    assert response.status_code == 200

@pytest.mark.django_db
def test_borrow_and_return_book(client, django_user_model):
    # create a user and log in
    user = django_user_model.objects.create_user(username='testuser', password='secret', email='test@example.com')
    client.login(username='testuser', password='secret')

    # create a book instance (assuming Book has fields: title and is_borrowed)
    book = Book.objects.create(title='Test Book', is_borrowed=False)

    # Borrow the book
    borrow_url = reverse('borrowed', kwargs={'title': book.title})
    response = client.get(borrow_url)
    assert response.status_code == 302
    book.refresh_from_db()
    assert book.is_borrowed is True
    borrow_record = Borrow.objects.get(book=book)
    assert borrow_record.user == user

    # Return the book
    return_url = reverse('return_book', kwargs={'title': book.title})
    response = client.get(return_url)
    assert response.status_code == 302
    book.refresh_from_db()
    assert book.is_borrowed is False
    with pytest.raises(Borrow.DoesNotExist):
        Borrow.objects.get(book=book)
