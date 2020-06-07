from django.contrib import admin
from django.urls import path

# MANUUALLY_____________
from generator import views
# MANUUALLY_____________ENDS__________


urlpatterns = [
    # path('admin/', admin.site.urls),

    # MANUUALLY_____________
    path('', views.home, name='home'),
    # generatedpassword/ is shown in browser
    # name='password' is REf name of that ulr to call on Form Action
    path('generatedpassword/', views.password, name='password'),
    path('about/', views.about, name='about')
    # MANUUALLY_____________ENDS__________
]
