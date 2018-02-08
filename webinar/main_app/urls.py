from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from .views import UserView, ExampleView, CategoryView, ProductView, BasketView

router = DefaultRouter()
router.register(r'users', UserView)
router.register(r'category', CategoryView)
router.register(r'product', ProductView)
router.register(r'example', ExampleView)
router.register(r'basket', BasketView, base_name='Basket')
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^auth/', obtain_jwt_token)
]