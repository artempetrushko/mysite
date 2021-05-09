from .models import User, MainCycle, Boost
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id']


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'cycle']


class CycleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCycle
        fields = ['id']


class CycleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCycle
        fields = ['id', 'user', 'coinsCount', 'clickPower', 'boosts']


class BoostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boost
        fields = ['id', 'mainCycle']


class BoostSerializerDetail(serializers.ModelSerializer):
    class Meta:
        model = Boost
        fields = ['id', 'boostNumber', 'mainCycle', 'level', 'power', 'price']

