from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    data = ProductSerializer(Product.objects.all().order_by('?').first()).data
    # instance = model_to_dict(Product.objects.all().order_by(
    #     '?').first(), fields=['id', 'title', 'price'])
    return Response(data)
