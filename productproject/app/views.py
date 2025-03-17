from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def Apioverview(req):
    api_urls={
        "all_products":"/AllProductview",
        "add_product":"/AddProduct",
        "update_product":"/UpdateProduct/update/pk",
        "delete_product":"/DeleteProduct/delete/pk",
        "search by category":"/searchbycategory/?category=category_name"
    }
    return Response(api_urls)

class AllProductview(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class AddProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


class UpdateProduct(generics.RetrieveUpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    partial=True

class DeleteProduct(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    # def destroy(self,request,*args,**kwargs):
    #     instance=self.get_object()
    #     instance.delete()
    #     return Response(print("product deleted"))

from rest_framework import status

# @api_view(["GET"])
# def searchbycategory(req):
#     if req.query_params:
#         items=Product.objects.filter(**req.query_params.dict())
#         serializer=ProductSerializer(items,many=True)
#         return Response(serializer.data)
#     else:
#         return Response(status=status.HTTP_404_NOT_FOUND)



# @api_view(["GET"])
# def searchbycategory(req):
#     if req.query_params:
#         items = Product.objects.filter(**req.query_params.dict())
        
#         if not items.exists():
#             return Response({"message": "No products found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = ProductSerializer(items, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     return Response({"error": "No query parameters provided"}, status=status.HTTP_400_BAD_REQUEST)


from django.db.models import Q

@api_view(["GET"])
def searchbycategory(req):
    query_params = req.query_params
    filters = Q()

    # **Category filtering**
    if "category" in query_params:
        filters &= Q(category=query_params["category"])

    # **Price filtering**
    min_price = query_params.get("min_price")
    max_price = query_params.get("max_price")

    if min_price and min_price.isdigit():
        filters &= Q(price__gte=min_price)

    if max_price and max_price.isdigit():
        filters &= Q(price__lte=max_price)

    # **Apply filters**
    items = Product.objects.filter(filters)

    if not items.exists():
        return Response({"message": "No products found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
