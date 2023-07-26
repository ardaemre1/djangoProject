from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from django.http import JsonResponse


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def get_products_by_category(request, category_name):
    try:
        url_friendly_category = category_name.lower().replace(' ', '')
        products = Product.objects.filter(product_name__icontains=url_friendly_category).order_by('product_name')
        
        product_list = []
        for product in products:
            product_data = {
                'id': product.id,
                'product_name': product.product_name,
                'price': product.price,
                'description': product.description,
                'brand': product.brand,
                'stock_status': product.stock_status,
                'stock_quantity': product.stock_quantity,
                # Diğer alanları ekleyebilirsiniz...
            }
            product_list.append(product_data)
        
        return JsonResponse(product_list, safe=False)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Ürün bulunamadı'}, status=404)