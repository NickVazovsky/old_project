from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from .views import (
    ProductView,
    BasketView,
    ProductCardView,
    OrderView,
    ProfileInformView,
    ProfileOrderView, )

router = DefaultRouter()
router.register(r'products', ProductView)
router.register(r'products_card', ProductCardView)
router.register(r'baskets', BasketView, )
router.register(r'orders', OrderView, base_name='order')
router.register(r'profile_inform', ProfileInformView, base_name='user')
router.register(r'profile/order', ProfileOrderView, base_name='profiles')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', obtain_jwt_token)
]
