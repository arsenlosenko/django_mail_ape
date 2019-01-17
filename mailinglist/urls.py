from django.urls import path

from mailinglist.views import (MailingListListView, CreateMailingListView,
                               DeleteMailingList, MailingListDetailView,
                               SubscribeToMailingListView,
                               ThankForSubscriptionView,
                               ConfirmSubscriptionView,
                               UnsubscribeView, CreateMessageView,
                               MessageDetailView)


app_name = "mailinglist"

urlpatterns = [
    path('', MailingListListView.as_view(), name="list-mailinglist"),
    path('new', CreateMailingListView.as_view(), name="create-mailinglist"),
    path('<uuid:pk>/delete', DeleteMailingList.as_view(), name="delete-mailinglist"),
    path('<uuid:pk>/manage', MailingListDetailView.as_view(), name="manage-mailinglist"),
    path('<uuid:mailinglist_id>/subscribe', SubscribeToMailingListView.as_view(), name="subscribe"),
    path('<uuid:pk>/thankyou', ThankForSubscriptionView.as_view(), name="subscriber-thankyou"),
    path('subscribe/confirmation/<uuid:pk>', ConfirmSubscriptionView.as_view(), name="confirm-subscription"),
    path('unsubscribe/<uuid:pk>', UnsubscribeView.as_view(), name="unsubscribe"),
    path('<uuid:mailinglist_pk>/message/new', CreateMessageView.as_view(), name="create-message"),
    path('message/<uuid:pk>', MessageDetailView.as_view(), name="view-message")
]
