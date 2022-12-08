from django.urls import path
from . import views


app_name = 'my_shop'
urlpatterns = [
    path('', views.allProCat, name='allProCat'),
    path('<slug:c_slug>/', views.allProCat, name='products_by_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.proDetails, name='products_details'),

]
