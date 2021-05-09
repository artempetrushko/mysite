from django.contrib.auth.models import User
from django.http import HttpResponse
from .models import MainCycle, Boost
from .serializers import UserSerializer, UserDetailSerializer, CycleSerializer, CycleDetailSerializer, BoostSerializer,\
    BoostSerializerDetail
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


class BoostList(generics.ListAPIView):
    queryset = Boost.objects.all()
    serializer_class = BoostSerializer


class BoostDetail(generics.RetrieveAPIView):
    queryset = Boost.objects.all()
    serializer_class = BoostSerializerDetail


def callClick(request):
    mainCycle = MainCycle.objects.filter(user=request.user)[0]
    mainCycle.Click()
    mainCycle.save()
    return HttpResponse(mainCycle.coinsCount)


def buyBoost(request):
    mainCycle = MainCycle.objects.filter(user=request.user)[0]
    boosts = Boost.objects.filter(mainCycle=mainCycle)
    if boosts.count() == 0:
        boost = Boost()
        boost.mainCycle = mainCycle
        boost.save()
        boost.Upgrade()
        mainCycle.save()
        return HttpResponse(mainCycle.clickPower)
    boost = boosts[0]
    boost.mainCycle = mainCycle
    boost.Upgrade()
    mainCycle.save()
    boost.save()
    return HttpResponse(mainCycle.clickPower)


def payForBoost(request):
    mainCycle = MainCycle.objects.filter(user=request.user)[0]
    return HttpResponse(mainCycle.coinsCount)

