from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Item

# Create your views here.

class Index(ListView):
    model = Item
    fields = '__all__'

class Add(CreateView):
    model = Item
    fields = '__all__'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def delete(request, wish_id):
    Item.objects.get(id=wish_id).delete()
    return redirect('index')
