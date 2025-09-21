from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.show_name, name='show_name'),
    path('create_product/', views.create_product, name="create_product"),
    path('product_list/', views.product_list,name="product_list"),
    path('products/<int:pk>', views.product_detail,name="product_detail"),
    path('xml/',views.show_xml,name="show_xml"),
    path('json/', views.show_json,name="show_json"),
    path('xml/<str:news_id>/',views.show_xml_by_id,name="show_xml_by_id"),
    path('json/<str:news_id>/',views.show_json_by_id,name="show_json_by_id"),
    path('register/', views.register,name="register"),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('employee/',views.add_employee, name='employee'),
    
]