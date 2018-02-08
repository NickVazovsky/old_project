from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from main_app.views import RouteView, TicketView, UserView


router = DefaultRouter()
router.register(r'routes', RouteView)
router.register(r'tickets', TicketView)
router.register(r'users', UserView)


urlpatterns = [
    # Auth:
    url(r'^auth/$', obtain_jwt_token),
    # Other endpoints:
    url(r'', include(router.urls))
]
urlpatterns+=router.urls
