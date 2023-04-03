import graphene
from contribution_plan.gql import ContributionPlanBundleGQLType
from core import prefix_filterset, ExtendedConnection
from core.gql_queries import UserGQLType
from graphene_django import DjangoObjectType
from insuree.schema import InsureeGQLType

from insuree_deceased.models import InsureeDeceased
from location.gql_queries import LocationGQLType


class InsureeDeceasedGQLType(DjangoObjectType):

    class Meta:
        model = InsureeDeceased
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            "id": ["exact"],
            "decease_date": ["exact", "lt", "lte", "gt", "gte"],
            "version": ["exact"],
            **prefix_filterset("insuree__", InsureeGQLType._meta.filter_fields),
            "date_created": ["exact", "lt", "lte", "gt", "gte"],
            "date_updated": ["exact", "lt", "lte", "gt", "gte"],
            "is_deleted": ["exact"]
        }

        connection_class = ExtendedConnection

    @classmethod
    def get_queryset(cls, queryset, info):
        return queryset
