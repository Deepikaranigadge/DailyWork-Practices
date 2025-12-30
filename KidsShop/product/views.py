from django.shortcuts import render
from  .models import Product
from django.db.models import Q


def products(request):
    template = 'products.html'
    product_list = Product.objects.all()

    # Search functionality
    query = request.GET.get('q')
    if query:
        product_list = product_list.filter(
            Q(title_icontains=query) |
            Q(description_icontains=query) |
            Q(category_icontains=query)
        )
        
        #Sort functionality (e.g by price or title)
        sort_by = request.GET.get('sort_by')
        if sort_by:
            product_list = product_list.order_by(sort_by)

            return render(request, template, {'products': product_list})

# Create your views here.
