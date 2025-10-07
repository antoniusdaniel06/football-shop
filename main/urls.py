from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.show_name, name='show_name'),
    path('create_product/', views.create_product, name="create_product"),
    path('create_car/', views.create_car, name="create_car"),
    path('products/<int:pk>', views.product_detail,name="product_detail"),
    path('xml/',views.show_xml,name="show_xml"),
    path('json/', views.show_json,name="show_json"),
    path('xml/<str:prod_id>/',views.show_xml_by_id,name="show_xml_by_id"),
    path('json/<str:prod_id>/',views.show_json_by_id,name="show_json_by_id"),
    path('register/', views.register,name="register"),
    path('login/', views.login_user,name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('employee/',views.add_employee, name='employee'),
    path('product/<int:pk>/edit', views.edit_product_ajax,name="edit_product_ajax"),
    path('product/<int:pk>/delete', views.delete_product_ajax, name='delete_product_ajax'),
    path('create-product-ajax', views.add_product_entry_ajax, name='add_product_entry_ajax'),
]