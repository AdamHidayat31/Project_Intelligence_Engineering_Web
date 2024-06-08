from django.urls import path
from . import views

urlpatterns =[
    path('',views.set_home,name='set_home'),

    path('meanob',views.set_ie,name='set_ie'),
    path('delete_ie/<int:id>/',views.delete_ie,name='delete_ie'),
    path('meanob/edit_ie/<int:id>/', views.edit_ie, name='edit_ie'),

    path('intexp',views.set_intexp, name='set_intexp'),
    path('delete_intexp/<int:id>/',views.delete_intexp,name='delete_intexp'),
    path('intexp/edit_intexp/<int:id>/', views.edit_intexp, name='edit_intexp'),

    path('intimp',views.set_intimp,name='set_intimp'),
    path('delete_intimp/<int:id>/',views.delete_intimp,name='delete_intimp'),
    path('intimp/edit_intimp/<int:id>/', views.edit_intimp, name='edit_intimp'),

    path('kendala', views. set_kendala, name='set_kendala'),
    path('delete_kendala/<int:id>/',views.delete_kendala,name='delete_kendala'),
    path('kendala/edit_kendala/<int:id>/', views.edit_kendala, name='edit_kendala'),

    path('status',views.set_status,name='set_status'),
    path('delete_status/<int:id>/',views.delete_status,name='delete_status'),
    path('status/edit_status/<int:id>/', views.edit_status, name='edit_status'),

    path('perimp',views.set_perimp,name='set_perimp'),
    path('delete_perimp/<int:id>/',views.delete_perimp,name='delete_perimp'),
    path('perimp/edit_perimp/<int:id>/', views.edit_perimp, name='edit_perimp'),
]