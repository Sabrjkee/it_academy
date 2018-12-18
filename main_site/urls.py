from django.urls import path

from main_site import views

# url(r'^ajax_calls/search/', views.autocompleteModel),
urlpatterns = [
    path('<int:pk>/mo/', views.MOListView.as_view(), name='mo_view'),
    path('', views.HomePage.as_view(), name='home'),
    # url(r'^ajax_calls/search/', views.HomePage.autocompleteModel,),
]

