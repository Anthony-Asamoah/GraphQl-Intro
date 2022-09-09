from ariadne import QueryType, ObjectType, gql, load_schema_from_path, make_executable_schema
from ariadne.asgi import GraphQL
from rest_framework import serializers
from . import models

import logging

from gql import models

schema = load_schema_from_path('gql/schema.gql')

query = QueryType()


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Restaurant
        fields = '__all__'


@query.field("restaurant")
def resolve_restaurant(_, info):
    expectation = [{
        'id': 0,
        'name': 'Two Sisters',
        'address': 'total, Abeka.',
        'chef': {
            'id': 0,
            'name': 'Anthony',
            'specialty': {
                'id': 0,
                'name': 'Jollof',
            }
        }
    }]

    result = [
        {
            'id': i.id,
            'name': i.name,
            'address': i.address,
            'chef': {k: v for k, v in i.chef_set.values()[0].items()}
        } for i in models.Restaurant.objects.all().prefetch_related('chef_set')
    ]

    for i in result:
        i['chef'].update({
            'specialty': {'id': a.id, 'name': a.name} for a in models.Specialty.objects.filter(id=i['chef']['work_id'])
        })

    return result


@query.field('chef')
def resolve_chef(_, info):
    expectation = [
        {
            'id': 0,
            'name': 'Tony',
            'work': {
                'id': 0,
                'name': 'Kanzo',
                'address': 'Tesano, Abeka',
            },
            'specialty': {
                'id': 0,
                'name': 'Noodles'
            }
        }
    ]

    result = [
        {
            'id': i.id,
            'name': i.name,
            'work': {
                'id': i.work.id,
                'name': i.work.name,
                'address': i.work.address
            },
            'specialty': {
                'id': i.specialty.id,
                'name': i.specialty.name
            }
        } for i in models.Chef.objects.all().select_related('work', 'specialty')
    ]

    return result


schema = make_executable_schema(schema, query)


