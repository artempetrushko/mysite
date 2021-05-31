from django.contrib.auth.models import User
from .models import MainCycle, Boost
from .serializers import UserSerializer, UserDetailSerializer, CycleSerializer, CycleDetailSerializer, BoostSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
import services


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

    def get_queryset(self):
        return Boost.objects.filter(mainCycle=self.kwargs['mainCycle'])


@api_view(['GET'])
def call_click(request):
    data = services.clicker_services.call_click(request)
    return Response(data)


@api_view(['POST'])
def buy_boost(request):
    main_cycle, level, price, power = services.clicker_services.buy_boost(request)
    return Response({'clickPower': main_cycle.clickPower,
                     'coinsCount': main_cycle.coinsCount,
                     'autoClickPower': main_cycle.autoClickPower,
                     'level': level,
                     'price': price,
                     'power': power})


@api_view(['POST'])
def set_maincycle(request):
    user = request.user
    data = request.data
    MainCycle.objects.filter(user=user).update(
        coinsCount=data['coinsCount']
    )
    return Response({'success': 'ok'})
