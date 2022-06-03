from django.urls import path
from . import views
#Urls.py file specifically for this app, will be connected to overall project in urls.py in mysite directory

#domain.com/first_app/
urlpatterns = [
    # path('', views.simple_view) #/my_apps -> PROJECT urls.py
    # path('sports/', views.sports_view),
    # path('finance/', views.finance_view)

    #Uses path converter to dynamically change content in this app
    # path('<int:num_page>', views.num_page_view),#for array of page numbers
    # path('<topic>/',views.news_view, name ='topic-page'),
    # path('<int:num1>/<int:num2>', views.add_view)


    #Linking view to template
    path('', views.simple_view)
    
]