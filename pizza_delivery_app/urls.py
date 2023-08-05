from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PizzaView

app_name = "pizza_delivery_app"

urlpatterns = [
    path('', PizzaView.as_view(), name='pizza-list'),

]


urlpatterns = format_suffix_patterns(urlpatterns)
