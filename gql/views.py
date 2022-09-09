from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import models


def index(request):

    return HttpResponse(f'''
    <h1 style='font-family: sans-serif; text-align: center;'>App Works</h1><br />
    <h3 style='color:gray; font-family: sans-serif; text-align:center'>Navigate to GraphQL Playground with
    <a href="/gql"><b>this link</b></a>
    </h3>
    ''')
