from django.conf.urls import url,include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from .views import ProductView, UserView, CategoryView, ExampleView


router = DefaultRouter()
#router.register(r'product', ProductView)
router.register(r'users', UserView)
router.register(r'categorys', CategoryView)
router.register(r'tickets', ProductView)
router.register(r'example', ExampleView)
#router.register(r'tickets/(?P<id>\d+$)', ProductView)


urlpatterns = [
    url(r'^auth/$', obtain_jwt_token),
   # url(r'^product/(?P<name>.+)/$', PurchaseList.as_view()),
    url(r'',include(router.urls))

]