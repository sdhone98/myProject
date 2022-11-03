from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['GET'])
def getData(request):
    partFamily = {
        'partFamilyName': 'Example_11',
        'shopTypes': ['engin', 'tyer', 'gear box'],
        'criticality': ['level_1', 'level_2', 'level_3'],
        'updatedBy': 'Owner',
        'updatedOn': '20-20-20'
    }

    return Response(partFamily)
