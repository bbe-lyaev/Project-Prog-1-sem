from django.urls import path

from django.contrib.auth.views import LogoutView
from .views import (
    create_new_person,
    PersonListView,
    PersonDetailsView,
    PersonDeleteView,
    PersonUpdateView,
    main_menu,
    HotelListView,
    HotelList,
    HotelUpdate,
    HotelDetailsView,
    LoginView,
    LogoutAndRedirectView,
)

app_name = "hotel"
urlpatterns = [
    path("", main_menu, name="main_menu"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutAndRedirectView.as_view(), name='logout'),
    path("person/", PersonListView.as_view(), name="person_list"),
    path("person/create", create_new_person.as_view(), name="create_new_person"),
    path("person/<int:pk>/", PersonDetailsView.as_view(), name="person_detail"),
    path("person/<int:pk>/delete", PersonDeleteView.as_view(), name="person_delete"),
    path("person/<int:pk>/update", PersonUpdateView.as_view(), name="person_update"),
    path("hotel", HotelListView.as_view(), name="hotel_list"),
    path("hotel/create", HotelList, name="hotel_create"),
    path("hotel/<int:pk>/update/", HotelUpdate, name="hotel_update"),
    path("hotel/<int:pk>/", HotelDetailsView.as_view(), name="hotel_detail"),
]