from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Todos
from .serializer import TodosSerializer


# Create your views here.
class TodosView(APIView):  
                
    def get(self,request,id =None): 
        if id:
            result = Todos.objects.get(id=id)
            serializers = TodosSerializer(result)
            return Response({'status': 'success', "todos":serializers.data}, status=200) 
        
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
        
    def patch(self, request, id):
        result = Todos.objects.get(id=id)
        serializer = TodosSerializer(result,data= request.data , partial= True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"sucess","data":serializer.data})
        else:
            return Response({"status":"error","data":serializer.errors})
        
    def delete(self, request, id=None):
        result = get_object_or_404(Todos, id=id) 
        result.delete()
        return Response({"status":"success","data":"Record Delete"})