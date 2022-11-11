from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import *
from .serializers import *
from django.views import View
from django.shortcuts import redirect, render


class DashboardView(View):
    def get(self,request):
        items = CryptoTable.objects.all().order_by('-id')
        return render(request,'home.html',{'items':items})

class CreateAndGetCryptoView(APIView):

    def get(self,request):
        cryptos = CryptoTable.objects.all().order_by('-id')
        serializer = CryptoSerializer(cryptos,many=True)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        """ 
        this post method to save data the following request - 
        {
            "data":[
                {
                    "name": "surya",
                    "price": 34,
                    "one_hour_per": 40,
                    "twenty_four_hour_per": 9,
                    "seven_day_per": 30,
                    "market_cap": 450,
                    "volume": 560,
                    "supply": 530
                },
                {
                    "name": "cvx",
                    "price": 34,
                    "one_hour_per": 40,
                    "twenty_four_hour_per": 9,
                    "seven_day_per": 30,
                    "market_cap": 450,
                    "volume": 560,
                    "supply": 530
                }
            ]
        }
        """
        response = []
        params=request.data['data']
        print("param",params)
        for data in params:
            serializer = CryptoSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            response.append(serializer.data)
        print("response",response)
        return Response({"data":response},status=status.HTTP_201_CREATED)


    