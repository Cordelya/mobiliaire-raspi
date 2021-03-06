from django.urls import path
from . import views

urlpatterns = [
        path('', views.index, name='index'),
        path('search/', views.search, name='search'),
        path('reports/', views.reports, name='reports'),
        path('items/', views.items, name='items'),
        path('items/<int:itemid>/', views.item, name='item'),
        path('boxes/', views.boxes, name='boxes'),
        path('boxes/<int:boxid>/', views.box, name='box'),
        path('warehouses/', views.warehouses, name='warehouses'),
        path('warehouses/<int:whid>/', views.warehouse, name='warehouse'),
        path('consumables/', views.consumables, name='consumables'),
        path('inventories/', views.inventory, name='inventories'),
        path('inventories/<int:invid>/', views.inventory, name='inventory'),
        path('keywords/', views.keywords, name='keywords'),
        path('reports/items/', views.report_itm, name='report_itms'),
        path('reports/box/<int:box>/', views.report_box, name='report_box'),
        path('reports/box/', views.report_box, name='report_boxes'),
        path('reports/wh/<int:whid>/', views.report_wh, name='report_wh'),
        path('reports/wh/', views.report_wh, name='report_whs'),
        path('reports/full/', views.report_full, name='report_full'),
        path('keyword/', views.keywords, name='keywords'),
        path('keyword/<str:kw_slug>/', views.keywords, name='keyword'),
        path('capture/<str:fileName>/', views.cameraCapture, name='piCapture'),
        path('capture/<str:fileName>/<str:fname>/', views.cameraCapture, name='pi_success'),
        ]
