from rest_framework.serializers import ModelSerializer
from drf_writable_nested import WritableNestedModelSerializer
from .models import Order, OrderItem

class OrderItemSerializer(ModelSerializer):
    class Meta:
        model = OrderItem
        exclube = ("order",)

class OrderSerializer(WritableNestedModelSerializer, ModelSerializer):
    items = OrderItemSerializer(many=True)


class Meta:
    model = Order
    fields = ("user", )