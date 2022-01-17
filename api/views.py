from .models import UUID
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.


class GetUUID(APIView):
    def get(self, request):
        UUID().save()
        json_array = []
        for i in UUID.objects.all():
            time_stamp = f'{i.time_stamp}'
            json_array.append({time_stamp.split("+")[0]: i.uuid})
        return Response(json_array)
