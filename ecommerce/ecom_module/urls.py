from django.conf.urls import url
from ecom_module import views

urlpatterns = [
    url(r'^deletecategory/$', views.DeleteCategory.as_view()),
    url(r'^addcategory/$', views.AddCategory.as_view()),
    url(r'^additems/$', views.AddItem.as_view()),
    url(r'^items/$', views.ItemList.as_view()),
    url(r'^items/(?P<pk>[0-9]+)/$', views.ItemDetail.as_view()),
    url(r'^category/$', views.CategoryList.as_view()),
    url(r'^category/(?P<pk>[0-9]+)/$', views.ItemList.as_view()),
    url(r'^cart/$', views.CartList.as_view()),
    url(r'^cart/(?P<pk>[0-9]+)/$', views.CartDetail.as_view()),
]




