from django.template.defaultfilters import slugify
import factory

import factory.fuzzy
from ..models import Nomspot

class NomspotFactory(factory.django.DjangoModelFactory):
    name = factory.fuzzy.FuzzyText()
    slug = factory.LazyAttribute(
        lambda obj: slugify(obj.name))

    description = factory.Faker(
        'paragraph', nb_sentences=3,
        variable_nb_sentences=True
    )
    goodness = factory.fuzzy.FuzzyChoice(
        [x[0] for x in Nomspot.Goodness.choices]
    )
    class Meta:
        model = Nomspot
