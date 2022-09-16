from django.contrib import admin
from django.urls import path, include
from caps import views
from caps.views import about,update_cap


urlpatterns = [
    path("",views.index, name='home'),
    path("home",views.index, name='home'),
    path("about",views.about, name='about'),
    path("login",views.login, name='login'),
    path("register",views.register, name='register'),
    path("create_caps",views.create_caps, name='create_caps'),
    path("show_caps",views.show_caps, name='show_caps'),
    path("most_viewed",views.most_viewed, name='most_viewed'),
    path("best_seller",views.best_seller, name='best_seller'),
    path("latest_arrivals",views.latest_arrivals, name='latest_arrivals'),
    path("cap_details/<id>",views.cap_details, name='cap_details'),
    path("cap_details/update_cap/<id>",views.update_cap, name='update_cap'),
    path("delete_cap/<id>",views.delete_cap, name='delete_cap'),
    path("create_order/<id>",views.create_order, name='create_order'),
    path("cart",views.cart, name='cart'),
    path("proceed_payment",views.proceed_payment,name='proceed_payment')

]