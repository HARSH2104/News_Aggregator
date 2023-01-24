
from django.urls import path
from news import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('', views.home,name="home" ),
    path('main',views.main,name="main" ),
    path('about',views.aboutx,name="about" ),
    path('sports',views.categories_sp,name="categories_sp"),
    path('politics',views.categories_po,name="categories_po"),
    path('education',views.categories_edu, name="categories_edu"),
    path('technology',views.categories_tec, name="categories_tec"),
    path('weather',views.categories_wea, name="categories_wea"),
    
    ] 
    
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)


    