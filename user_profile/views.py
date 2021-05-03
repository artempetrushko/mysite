from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import MainCycle, Boost
from .serializers import UserSerializer, UserDetailSerializer, CycleSerializer, CycleDetailSerializer
from rest_framework import generics


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CycleList(generics.ListAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleSerializer


class CycleDetail(generics.RetrieveAPIView):
    queryset = MainCycle.objects.all()
    serializer_class = CycleDetailSerializer


def callClick(request):
    mainCycle = MainCycle.objects.filter(user=request.user)[0]
    mainCycle.Click()
    mainCycle.save()
    return HttpResponse(mainCycle.coinsCount)


def buyBoost(request):
    mainCycle = MainCycle.objects.filter(user=request.user)[0]
    boost = Boost()
    boost.mainCycle = mainCycle
    boost.save()
    boost.Upgrade()
    mainCycle.save()
    return HttpResponse(mainCycle.clickPower)

