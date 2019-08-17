from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm
from .forms import BookCreateForm
from django.views.generic import *
from django.views.generic.base import View
from django.urls import reverse_lazy



def index(request):
    template = 'list.html'
    book = Book.objects.all()
    context = {'book': book}
    return render(request, template, context)


def book_create(request):
    template = 'form.html'
    form = BookForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fcrudapp:home')

    context = {"form1": form}
    return render(request, template, context)


def book_update(request, pk):
    template = 'form.html'
    book = get_object_or_404(Book, pk=pk)
    print(book, '*narendra*')
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('fcrudapp:home')
    context = {"form": form}
    return render(request, template, context)


def book_delete(request, pk):
    template = 'delete.html'
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('fcrudapp:home')
    context = {'book': book}
    return render(request, template, context)


class BookDetailView(DetailView):
    template_name='bookdetail.html'
    model=Book
    context_object_name='bookdetail'

class BookCreateView(CreateView):
    def get(self,request,*args,**kwargs):
        context={'form':BookCreateForm()}
        return render(request,'bookcreate.html',context)
    def post(self,request,*args,**kwargs):
        form=BookCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request,'bookcreate.html',{'form':form})







