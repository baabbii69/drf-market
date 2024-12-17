from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import OrderListAPIViewSet, ProductListAPIViewSet

router = DefaultRouter()
router.register(r'products', ProductListAPIViewSet, basename='products')  # List and create products # Retrieve single product
router.register(r'orders', OrderListAPIViewSet, basename='orders')  # Orders

urlpatterns = router.urls

# urlpatterns = [
#     path('products/', views.ProductList.as_view()),
#     path('order/', views.OrderList.as_view()),
#     path('orders/', views.OrderListAPIView.as_view()),
#     path('products/<int:pk>/', views.ProductDetail.as_view()),
# ]
