from django.urls import path

from api.views import (MailingListCreateListView,
                       MailingListRetriveUpdateDestroyView,
                       SubscriberListCreateView,
                       SubscriberRetrieveUpdateDestroyView, api_root)

app_name = "api"

urlpatterns = [
    path('', api_root, name="api-root"),
    path('mailinglists', MailingListCreateListView.as_view(), name="mailinglist-list"),
    path('mailinglists/<uuid:pk>', MailingListRetriveUpdateDestroyView.as_view(), name="mailinglist-detail"),
    path('mailinglists/<uuid:mailinglist_pk>/subscribers', SubscriberListCreateView.as_view(), name="subscriber-list"),
    path('subscribers/<uuid:pk>', SubscriberRetrieveUpdateDestroyView.as_view(), name="subscriber-detail"),
]
