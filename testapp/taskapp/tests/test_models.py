import pytest
from taskapp.factories import DBTestDataBaseFactory, DBTestTestFactory


@pytest.mark.django_db
def test_datainfotemp_creation():
    """ Test creation of DataInfoTemp model and ensure proper database entry is created """
    datainfo = DBTestDataBaseFactory()
    datainfo.user_id = 1000
    datainfo.type = "new_type"
    datainfo.save()
    assert datainfo.user_id == 1000
    assert datainfo.type == "new_type"


@pytest.mark.django_db
def test_datatemp_creation():
    datainfo = DBTestDataBaseFactory()
    data_temp = DBTestTestFactory(data_info=datainfo)
    data_temp.date = "product"
    data_temp.value = "4"
    data_temp.save()
    assert data_temp.date == "product"
    assert data_temp.value == "4"
