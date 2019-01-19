import base64
import json

from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APITestCase

from mailinglist.models import MailingList


class TestListMailingListAPI(APITestCase):

    def setUp(self):
        password = 'password'
        username = 'unit test'
        self.user = get_user_model().objects.create_user(
            username=username,
            password=password
        )
        cred_bytes = '{}:{}'.format(username, password).encode('utf-8')
        self.basic_auth = base64.b64encode(cred_bytes).decode('utf-8')

    def test_list_all_mailinglists(self):
        mailing_lists = [
            MailingList.objects.create(
                name="unit test {}".format(n),
                owner=self.user
            )
            for n in range(3)
        ]

        self.client.credentials(
            HTTP_AUTHORIZATION='Basic {}'.format(self.basic_auth)
        )

        mailinglists_url = reverse(
            'api:mailinglist-list'
        )

        response = self.client.get(mailinglists_url)

        self.assertEqual(200, response.status_code)
        parsed = json.loads(response.content)
        self.assertEqual(3, len(parsed))

        content = str(response.content)
        for ml in mailing_lists:
            self.assertIn(str(ml.id), content)
            self.assertIn(ml.name, content)
