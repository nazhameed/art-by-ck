from django.urls import path
from .views import ContactFormView, contact_form_ajax

app_name = 'contactform'

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact_form'),
]
