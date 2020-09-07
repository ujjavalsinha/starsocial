from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
from django.urls import reverse_lazy

app_name = 'accounts'

urlpatterns = [
    url('signup/', views.SignUp.as_view(), name = 'signup'),
    url('login/', login, {'template_name': 'accounts/login.html'}, name='login'),
    url('logout/', logout, {'next_page': reverse_lazy('home')}, name='logout'),

]
