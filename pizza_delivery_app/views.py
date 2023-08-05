from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response


from .serializers import PizzaSerializer
# Create your views here.


class PizzaView(generics.ListCreateAPIView):
    serializer_class = PizzaSerializer

    def get_queryset(self):
        serializer = self.serializer_class()
        queryset = serializer.get()
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        return Response(queryset, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            pizza = serializer.save()
            response = serializer.data
            return Response(response, status=status.HTTP_201_CREATED)
        
        return Response({'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    

