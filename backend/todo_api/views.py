from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todos
from .serializer import TodosSerializer


# Create your views here.
class TodosView(APIView):  
  
    def get(self, request, *args, **kwargs):  
        result = Todos.objects.all()  
        serializers = TodosSerializer(result, many=True)  
        return Response({'status': 'success', "todos":serializers.data}, status=200)  
  
    def post(self, request):  
        serializer = TodosSerializer(data=request.data)  
        if serializer.is_valid():  
            serializer.save()  
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  