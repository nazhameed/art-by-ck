from django.urls import path
from .views import ContactFormView

app_name = 'contactform'

urlpatterns = [
    path('', ContactFormView.as_view(), name='contact_form'),
]
