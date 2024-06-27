from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

app_name='tiendita'

urlpatterns = [
    path('', views.index, name='index'),
    # paths de autenticacion
    path('registrar/', views.registrar, name='registrar'),
    path('login/', views.login, name='login'),

    #paths del menu
    path('categorias/', views.listCategorias, name='categorias'),
    path('contacto/', views.contacto, name='contacto'),
    path('garantia/', views.garantia, name='garantia'),
    path('devoluciones/', views.devoluciones, name='devoluciones'),
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