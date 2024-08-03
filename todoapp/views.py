from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .serializers import TodoSerializer, CategorySerializer

from .models import Todo, Category


class TodoCreateView(generics.CreateAPIView):
    serializer_class = TodoSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Todo Created Succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CategoryCreateView(generics.CreateAPIView):
    serializer_class = CategorySerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message" : "Category Created Succesfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TodoListView(generics.ListAPIView):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

class CategoryListView(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)