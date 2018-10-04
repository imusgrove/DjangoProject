from django.conf.urls import url

from . import views

app_name = 'addressBook'

urlpatterns = [
    # defaulting to viewing all contacts
    url('', views.contact_list, name='contact_list'),
    # view specific contact
    url(r'^person/<int:pk>', views.contact_detail, name='contact_detail'),
    # new contact
    url(r'^person/new', views.contact_new, name='contact_new'),
    # edit contact
    url(r'^person/<int:pk>/edit', views.contact_edit, name='contact_edit'),
    # delete contact
    url(r'^person/<int:pk>/delete', views.reverse_lazy, name='contact_delete'),
    

]