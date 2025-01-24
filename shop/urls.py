from django.urls import path

from . import views


urlpatterns = [
    path("", views.ItemsView.as_view(), name="home_page"),
    path("filter/", views.FilterItemsView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path("<slug:slug>/", views.ItemDetailView.as_view(), name="item_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("vendor/<str:slug>/", views.VendorView.as_view(), name="vendor_detail"),
]
