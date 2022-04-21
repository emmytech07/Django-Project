from django.urls import path
from . views import CustomAuthToken, Investorsignup, Inventorsignup,LogOutView,InventorOnly,InvestorOnly


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', views.allroutes, name="allroutes"),
    path('signup/inventors/', Inventorsignup.as_view()),
    path('signup/investors/', Investorsignup.as_view()),
    path('login/', CustomAuthToken.as_view(), name="auth_token"),
    path('logout/', LogOutView.as_view(), name="logout"),
    path('inventor-dash/', InventorOnly.as_view(), name="inventor-view"),
    path('investor-dash/', InvestorOnly.as_view(), name="investor-view")
]