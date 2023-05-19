from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status, viewsets
from . import models, serializers
import random


class SeruViewSet(viewsets.ModelViewSet):
    queryset = models.Seru.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    serializer_class = serializers.SeruSerializer


@api_view(['GET'])
def chelseru_beyr(_):
    chelseru_count = 11
    objs = models.Seru.objects.all()
    chelserus = list()
    while len(chelserus) < chelseru_count:
        obj = random.choice(objs)
        ser = serializers.SeruSerializer(instance=obj)

        if ser.data not in chelserus:
            if len(chelserus) == chelseru_count-1:
                result = list()
                result.append({'39': chelserus})
                result.append({'40': ser.data})
                return Response(data=result, status=status.HTTP_200_OK)
            chelserus.append(ser.data)

    # if len(chelserus) == chelseru_count-1:
    return Response(data={'error': 'text error'}, status=status.HTTP_502_BAD_GATEWAY)