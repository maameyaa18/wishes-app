from django.urls import path
from .import views

app_name = 'wishes'

urlpatterns = [
    #Homepage
    path('', views.index, name='index'),

    # Wishes Page
    path('all_wishes/', views.all_wishes, name='all_wishes'),

    #New Wish
    path('new_wish/', views.new_wish, name= 'new_wish'),

    #Detail Wish
    path('all_wishes/<detail_id>/', views.detail, name='detail'),

    #My Wishes
    path('my_wishes/', views.my_wishes, name='my_wishes'),

    #Edit Wish
    path('edit_wish<edit_id>/', views.edit_wish, name='edit_wish'),

    #Delete Wish
    path('delete_wish/<delete_id>/', views.delete_wish, name='delete_wish')  
    
]