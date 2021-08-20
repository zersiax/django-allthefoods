import pytest

pytestmark = pytest.mark.django_db
from ..models import Nomspot

def test__str__():

    nom = Nomspot.objects.create(
        name="testface",
        description="Eat your testeburgers here.",
        goodness=Nomspot.Goodness.UNSPECIFIED,
    )
    assert nom.__str__() == "testface"
    assert str(nom) == "testface"


