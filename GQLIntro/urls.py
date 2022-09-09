from django.contrib import admin
from django.urls import path, include
from ariadne_django.views import GraphQLView

from gql import views as gql
from gql.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', gql.index, name='index'),
    path('gql/', GraphQLView.as_view(schema=schema), name='gql')
]
