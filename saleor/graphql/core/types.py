import graphene
from django_prices.templatetags import prices_i18n
from graphene_django import DjangoObjectType


class CountableConnection(graphene.relay.Connection):
    class Meta:
        abstract = True

    total_count = graphene.Int()

    @staticmethod
    def resolve_total_count(root, info, *args, **kwargs):
        return root.length


class CountableDjangoObjectType(DjangoObjectType):
    class Meta:
        abstract = True

    @classmethod
    def __init_subclass_with_meta__(cls, *args, **kwargs):
        # Force it to use the countable connection
        countable_conn = CountableConnection.create_type(
            "{}CountableConnection".format(cls.__name__),
            node=cls)
        super().__init_subclass_with_meta__(
            *args, connection=countable_conn, **kwargs)


class Error(graphene.ObjectType):
    field = graphene.String()
    message = graphene.String()


class Money(graphene.ObjectType):
    currency = graphene.String()
    amount = graphene.Float()
    localized = graphene.String()

    def resolve_localized(self, info):
        return prices_i18n.amount(self)


class TaxedMoney(graphene.ObjectType):
    currency = graphene.String()
    gross = graphene.Field(Money)
    net = graphene.Field(Money)


class TaxedMoneyRange(graphene.ObjectType):
    start = graphene.Field(TaxedMoney)
    stop = graphene.Field(TaxedMoney)
