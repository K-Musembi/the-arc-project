#!/usr/bin/env python3
"""views module"""

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, authenticate, login as auth_login
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Book, Borrow

User = get_user_model()


def home(request):
    """home page view"""
    books = Book.objects.all()
    return render(request, 'home.html', {'books': books})

def signup_view(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')

def signup(request):
    """sign up view"""
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('signup_view')
        
        user = User.objects.create_user(
            username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Account created successfully')
        return redirect('login_view')
    
    return redirect('signup_view')

def login(request):
    """login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user:
            auth_login(request, user)
            return redirect('profile', username=username)
    return redirect('login_view')

def profile(request, username):
    """user profile view"""
    user = get_object_or_404(User, username=username)
    borrowed_books = Borrow.objects.filter(user=user)

    return render(request, 'profile.html', borrowed_books)

def borrowed(request, title):
    book = get_object_or_404(Book, title=title)
    if book.is_borrowed:
        messages.error(request, 'This book has already been borrowed')

    borrow_record = Borrow.objects.create(user=request.user, book=book)
    # Django will add the user and book id's as foreign keys
    book.is_borrowed = True
    borrow_record.save()
    
    messages.success(request, f"You have successfully borrowed {book.title}.")
    return redirect('profile', username=request.user.username)

def return_book(request, title):
    """return view"""
    book = get_object_or_404(Book, title=title)
    borrow_record = Borrow.objects.get(book=book)
    book.is_borrowed = False
    borrow_record.delete()

    messages.success(request, f"You have successfully returned {book.title}.")
    return redirect('profile', username=request.user.username)
