import datetime
import json
import warnings
from dataclasses import dataclass

from django.conf import settings
from django.test import TestCase
from graphene_django.utils import GraphQLTestCase
from graphql_jwt.shortcuts import get_token
from rest_framework import status

from core.models import User
from core.schema import core
from core.test_helpers import create_test_interactive_user
from insuree.test_helpers import create_test_insuree
from insuree_deceased.models import InsureeDeceased
from insuree_deceased.services import DeceasedInsureeService


@dataclass
class DummyContext:
    """ Just because we need a context to generate. """
    user: User


class ExampleImisTest(GraphQLTestCase):
    GRAPHQL_URL = f'/{settings.SITE_ROOT()}graphql'
    # This is required by some version of graphene but is never used. It should be set to the schema but the import
    # is shown as an error in the IDE, so leaving it as True.
    GRAPHQL_SCHEMA = True
    admin_user = None

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.admin_user = create_test_interactive_user(username="testLocationAdmin")
        cls.admin_token = get_token(cls.admin_user, DummyContext(user=cls.admin_user))
        cls.test_insuree = create_test_insuree(with_family=True, custom_props={"dob": core.datetime.date(1985, 5, 5)})
        cls.test_decease_date = InsureeDeceased(
            decease_date=datetime.datetime(2023, 3, 17),
            insuree=cls.test_insuree
        )

    def test_query_insuree_number_validity(self):
        response = self.query(
            '''
             query (
                  $insuree_Uuid: String
                  ) {
                  insureeDeceased (insuree_Uuid:$insuree_Uuid) {
                    edges {
                      node {
                        deceaseDate
                      }
                    }
                  }
                }
            ''',
            variables={'insuree_Uuid': self.test_insuree.uuid},
            headers={"HTTP_AUTHORIZATION": f"Bearer {self.admin_token}"},
        )

        self.assertEquals(response.status_code, status.HTTP_200_OK)
        content = json.loads(response.content)

        self.assertResponseNoErrors(response)
