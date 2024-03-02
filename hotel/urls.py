from django.urls import path
from .views import RoomList, BookingList,BookingView

app_name='hotel'

urlpatterns=[
    path('room_list/',RoomList.as_view(), name='RoomList'), #view er Roomlist ke room_list hishebe view korbe
    path('booking_list/',BookingList.as_view(), name='BookingList'), # view er BookingList ke booking_list hishebe url nibe 
    path('book/',BookingView.as_view(), name='booking_view'),
]