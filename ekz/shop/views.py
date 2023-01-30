from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import CreateView

from .forms import Registration, ProductsForm
from .models import Product


class Index(generic.ListView):
    model = Product
    template_name = 'index.html'


class Products(generic.ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'


class RegisterUser(generic.CreateView):
    form_class = Registration
    template_name = 'registration.html'
    success_url = reverse_lazy('login')
    success_page = 'registration'


class Profile(generic.ListView):
    model = Product
    template_name = 'profile.html'


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = Product
    template_name = 'product.html'


def create_project(request):
    if request.method == 'POST':
        if not Product.objects.all():
            return render(request, 'errors/category_error.html')
        else:
            form = ProductsForm(request.POST, request.FILES)
            if form.is_valid():
                Application = form.save(commit=False)
                Application.save()
                return redirect(reverse_lazy('profile'))
    else:
        form = ProductsForm()

    return render(request, 'order.html', {'form': form})

# class CreateProduct(CreateView):
#     template_name = 'order.html'
#     # model = Product
#     # fields = ('name', 'description', 'image')
#     form_class = Products
#     success_url = reverse_lazy('profile')
