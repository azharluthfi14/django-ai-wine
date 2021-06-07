from django.urls import path
from . import views, auth
from django.contrib.auth.decorators import login_required
from . views import (
    LandingPageView,
    DashboardView,
    FormView,
)

app_name = 'app'

urlpatterns = [

    path('', LandingPageView.as_view(), name='index'),
    path('signup', auth.user_register, name='signup'),
    path('signin', auth.user_login, name='signin'),
    path('user/profile/<username>', auth.user_profile, name='profile'),
    path('user/logout/', auth.user_logout, name='logout'),
    path('dashboard/', login_required(DashboardView.as_view()), name='dashboard'),
    path('classification/create', login_required(FormView.as_view()), name='predict'),
    path('user/classification/submit',
         views.predict_submit, name='submit_predict'),
    path('result/', views.data_wine, name='data-results'),

]
