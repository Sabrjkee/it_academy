from django.urls import path


from IT import views


urlpatterns = [
    path('equipment/<int:pk>/', views.EqipmentView.as_view(), name='equipment'),
    path('network/<int:pk>/', views.NetworkView.as_view(), name='network'),
    path('provider/<int:pk>/', views.ProviderView.as_view(), name='provider'),

]