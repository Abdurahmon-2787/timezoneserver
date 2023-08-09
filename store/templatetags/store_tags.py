from django import template

from ..models import Category, FavouriteProducts

register = template.Library()


@register.simple_tag()
def get_all_categories():
    categories = Category.objects.filter(parent=None)
    return categories


@register.simple_tag()
def get_sorted():
    sorters = [
        {
            'title': "Narxi bo'yicha",
            'sorters': [
                'price', 'O\'sish'
            ]
        },
        {
            'title': "Ommaboplari",
            'sorters': [
                'popular', 'Ommabop'
            ]
        }
    ]


@register.simple_tag()
def get_favourite_products(user):
    fav = FavouriteProducts.objects.filter(user=user)
    products = [i.product for i in fav]
    return products

