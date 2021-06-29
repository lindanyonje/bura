from django.urls import path
# from . import views
from shop.views import CategoryDelete, CategoryUpdate, CategoryList,CategoryDetail ,CategoryCreate, SimpleFormView
from shop.views import SellerDelete, SellerUpdate, SellerList, SellerDetail,SellerCreate
from shop.views import ProductDelete, ProductUpdate,ProductList, ProductDetail,ProductCreate

urlpatterns=[
    path('categories/',CategoryList.as_view(),name="category_list"),
    path('category/detail/<pk>',CategoryDetail.as_view(),name= 'category_detail'),
    path('create/category', CategoryCreate.as_view(),name= 'category_create'),
    path('update/category/<pk>/',CategoryUpdate.as_view(),name='category_update'),
    path('delete/category/<pk>/',CategoryDelete.as_view(),name='category_delete'),
    path('sellers/',SellerList.as_view(),name="Seller_list"),
    path('seller/detail/<pk>',SellerDetail.as_view(),name= 'Seller_detail'),
    path('create/seller', SellerCreate.as_view(),name= 'Seller_create'),
    path('update/seller/<pk>/',SellerUpdate.as_view(),name='Seller_update'),
    path('delete/seller/<pk>/',SellerDelete.as_view(),name='Seller_delete'),
    path('products/',ProductList.as_view(),name="Product_list"),
    path('Product/detail/<pk>',ProductDetail.as_view(),name= 'Product_detail'),
    path('create/Product', ProductCreate.as_view(),name= 'Product_create'),
    path('update/Product/<pk>/',ProductUpdate.as_view(),name='Product_update'),
    path('delete/Product/<pk>/',ProductDelete.as_view(),name='Product_delete'),
    



]