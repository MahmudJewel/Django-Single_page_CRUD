from django.urls import path, include
from second.views import home_view, home_view_fnc
from django.views.generic import DeleteView

urlpatterns = [
    path('', home_view.as_view()),
    path('1', home_view_fnc, name="hm"),
    # path('delete', DeleteView.as_view()),
]
