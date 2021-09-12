# importing Django's function path
from django.urls import path
# and importing all of our views from the blog application. (We don't have any yet, but we will get to that in a minute!)
from . import views


# we're now assigning a view called post_list to the root URL. This URL pattern will match an empty string and the Django URL resolver will ignore the domain name
urlpatterns = [
    path('', views.post_list, name='post_list'),
]