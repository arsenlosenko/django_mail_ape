from django.shortcuts import get_object_or_404
from django.urls import reverse

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse as api_reverse
from rest_framework.generics import (ListCreateAPIView,
                                     RetrieveUpdateDestroyAPIView)

from api.permissions import CanUseMailingList
from api.serializers import (MailingListSerializer, SubscriberSerializer,
                             ReadOnlyEmailSubscriberSerializer)

from mailinglist.models import MailingList, Subscriber


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'mailinglists': api_reverse('api:mailinglist-list', request=request, format=format),
    })


class MailingListCreateListView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, CanUseMailingList)
    serializer_class = MailingListSerializer

    def get_queryset(self):
        return self.request.user.mailinglist_set.all()


class MailingListRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, CanUseMailingList)
    serializer_class = MailingListSerializer
    queryset = MailingList.objects.all()


class SubscriberListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, CanUseMailingList)
    serializer_class = SubscriberSerializer

    def get_queryset(self):
        mailinglist_pk = self.kwargs['mailinglist_pk']
        mailing_list = get_object_or_404(MailingList, id=mailinglist_pk)
        return mailing_list.subscriber_set.all()

class SubscriberRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, CanUseMailingList)
    serializer_class = ReadOnlyEmailSubscriberSerializer
    queryset = Subscriber.objects.all()
