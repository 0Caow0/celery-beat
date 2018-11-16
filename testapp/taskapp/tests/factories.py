import factory

from taskapp.models import DBTestDataBase, DBTestTest


class DBTestDataBaseFactory(factory.DjangoModelFactory):
    """
        Define datainfotemp Factory
    """
    class Meta:
        model = DBTestDataBase


class DBTestTestFactory(factory.DjangoModelFactory):
    """
        Define temp data Factory
    """
    class Meta:
        model = DBTestTest
    data_info = factory.SubFactory(DBTestDataBaseFactory)
