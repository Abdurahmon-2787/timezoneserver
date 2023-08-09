from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib import messages
from django.contrib.auth import logout, login

from .models import *
from .forms import *
from .utils import *


class ProductList(ListView):
    model = Product
    context_object_name = 'categories'
    template_name = 'store/index.html'

    extra_context = {
        'title': 'TIME ZONE: Bosh sahifa'
    }

    def get_queryset(self):
        return Category.objects.filter(parent=None)


class ProductListByCategory(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'store/category_products.html'

    def get_queryset(self):
        category = Category.objects.get(slug=self.kwargs['slug'])
        subcategories = category.subcategory.all()
        products = Product.objects.filter(category__in=subcategories)
        # sorted_file = self.request.GET.get('sort')
        # if sorted_file:
        #     products = products.order_by(sorted_file)
        return products

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = f"Kategoriya: {Category.objects.get(slug=self.kwargs['slug']).title}"
        return context


class about_us(ListView):
    model = Product
    context_object_name = 'about'
    template_name = 'store/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = f"Biz haqimizda:"
        return context


class ProductDetail(DetailView):
    model = Product
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = Product.objects.get(slug=self.kwargs['slug']).title
        context['reviews'] = Review.objects.filter(product__slug=self.kwargs['slug'], publish=True)
        reviews = Review.objects.filter(product__slug=self.kwargs['slug'], publish=True)
        if reviews.count() > 0:
            context['reviews'] = reviews
        products = Product.objects.filter(quantity__gt=0)
        data = []
        for i in range(2):
            from random import randint
            random_index = randint(0, len(products) - 1)
            product = products[random_index]
            if product not in data:
                data.append(product)
        context['products'] = data
        if self.request.user.is_authenticated:
            context['review_form'] = ReviewForm()
        return context


def user_login(request):
    form = LoginForm(data=request.POST)
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        return redirect('index')
    else:
        messages.error(request, "Loginda yoki parolda hatolik mavjud!")
        return redirect('login_registration')


def user_logout(request):
    logout(request)
    return redirect('index')


def register(request):
    form = RegistrationForm(data=request.POST)
    if form.is_valid():
        user = form.save()
        messages.success(request, 'Ro\'yxatdan o\'tdingiz!')
    else:
        for error in form.errors:
            messages.error(request, form.errors[error][0])
    return redirect('login_registration')


def login_registration(request):
    context = {
        'login_form': LoginForm(),
        'register_form': RegistrationForm(),
        'title': "Kirish yoki ro'yxatdan o'tish"
    }
    return render(request, 'store/login_registration.html', context)


def save_review(request, product_slug):
    form = ReviewForm(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.author = request.user
        product = Product.objects.get(slug=product_slug)
        review.product = product
        review.save()
    else:
        messages.error(request, "Hatolik mavjud!")

    return redirect('product_detail', product_slug)


def save_or_delete_fav_products(request, product_slug):
    user = request.user if request.user.is_authenticated else None
    product = Product.objects.get(slug=product_slug)

    if user:
        favourite_products = FavouriteProducts.objects.filter(user=user)
        if product in [i.product for i in favourite_products]:
            fav_product = FavouriteProducts.objects.get(user=user, product=product)
            fav_product.delete()
        else:
            FavouriteProducts.objects.create(user=user, product=product)
    next_page = request.META.get('HTTP_REFERER', 'index')
    return redirect(next_page)


class FavouriteProductList(ListView):
    model = FavouriteProducts
    context_object_name = 'products'
    template_name = 'store/favourite_products.html'

    def get_queryset(self):
        user = self.request.user
        fav = FavouriteProducts.objects.filter(user=user)
        products = [i.product for i in fav]
        return products


def cart(request):
    cart_info = get_cart_data(request)

    context = {
        'cart_total_quantity': cart_info['cart_total_quantity'],
        'order': cart_info['order'],
        'products': cart_info['products'],
    }
    return render(request, 'store/cart.html', context)


def to_cart(request, product_id, action):
    if request.user.is_authenticated:
        user_cart = CartForAuthenticatedUser(request, product_id, action)
        return redirect('cart')
    else:
        messages.error(request, "Avtorizatsiyadan yoki ro'yxatdan o'ting")
        return redirect('login_registration')


def checkout(reqeust):
    cart_info = get_cart_data(reqeust)
    context = {
        'cart_total_quantity': cart_info['cart_total_quantity'],
        'order': cart_info['order'],
        'products': cart_info['products'],
        'customer_form': CustomerForm(),
        'shipping_form': ShippingForm(),
        'title': "Buyurtmani tasdiqlash"
    }
    return render(reqeust, 'store/checkout.html', context)


class Contact(ListView):
    model = Contacts
    template_name = 'store/contact.html'
    context_object_name = 'contacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['title'] = f"Biz bilan bog'laning:"
        context['form'] = ContactForm()
        return context


def save_contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            user = request.user
            contact.author = user
            contact.save()
            return redirect('index')
        else:
            messages.error(request, 'Hato')
            return redirect('contact')

# def index(request):
#     products = Product.objects.all()
#     categories = Category.objects.filter(parent=None)
#     context = {
#         'categories': categories,
#         'products': products,
#         'title': 'TIME_ZONE Bosh sahifa'
#     }
#     return render(request, 'store/index.html', context)
