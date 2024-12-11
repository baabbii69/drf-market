from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderListAPIViewSet, ProductListAPIViewSet, ProductDetailAPIViewSet

router = DefaultRouter()
router.register(r'orders', OrderListAPIViewSet, basename='orders')
router.register(r'products', ProductListAPIViewSet, basename='products')
router.register(r'products', ProductDetailAPIViewSet, basename='product')

urlpatterns = router.urls

# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('order/', views.OrderList.as_view()),
#     path('orders/', views.OrderListAPIView.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
# ]
