from django.urls import path , include
from . import views
from django.contrib.auth.views import LoginView
from .views import CustomLogoutView


app_name='tiendita'

urlpatterns = [
    path('', views.index, name='index'),
    # paths de autenticacion
    path('registrar/', views.registrar, name='registrar'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/', include('django.contrib.auth.urls')),

    #paths del menu
    path('categorias/', views.listCategorias, name='categorias'),
    path('nosotros/', views.nosotros, name='nosotros'),

    #paths edicion de productos
    path('producto/', views.detalleProducto, name='producto'),
    path('addproducto/', views.addProducto, name='addproducto'),
    path('detalleproducto/<id>/', views.detalleProducto, name='detalleproducto'),
    path('productocategoria/<id>/', views.productoxCategoria, name='productocategoria'),
    path('editproducto/<id>/', views.editarProducto, name='editproducto'),
    path('deleteProducto/<id>/', views.deleteProducto, name='deleteProducto'),
    path('listarproductos/', views.listarProductos, name='listarproductos'),
    path('addcategoria/', views.addCategoria, name='addcategoria'),
    path('editcategoria/<id>/', views.modificarCategoria, name='editcategoria'),
    path('deleteCategoria/<id>/', views.deleteCategoria, name='deleteCategoria'),
    
    #Paths del carrito
    path('viewcart/', views.viewcart, name="viewcart"),
    path('addcart/<producto_id>/', views.agregar_producto, name="addcart"),
    path('delcart/<producto_id>/', views.eliminar_producto, name="delcart"),
    path('restarcart/<producto_id>/', views.restar_producto, name="restarcart"),
    path('cleancart/', views.cleancart, name="cleancart"),
    path('procesar_compra/', views.procesar_compra, name="procesar_compra"),
    
]