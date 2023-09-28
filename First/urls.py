"""
URL configuration for First project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from First import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('index/', views.homePage),
    path('', views.homePage),
    path('detail/<int:courseid>',views.detail),
    path('about/', views.about),   
    path('menu/', views.menu),
    path('booking/', views.booking),
    path('service/', views.service),
    path('team/', views.team),
    path('savebooking/', views.saveBooking,name='savebooking'),
    path('testimonial/', views.testimonial),
    path('contact/', views.contact),
    path('adminPanel/', views.adminPanel),
    path('viewBookings/', views.viewBookings),
    path('viewChefs/', views.viewChefs),
    path('AddChefs/', views.AddChefs,name='AddChefs'),
    
    path('Chef/', views.chef),
             
]


# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('about-us/', include('First.urls', namespace='first')),
# ]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
