from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from rest_framework import status
from .models import Item
from .serializer import ItemSerializer, ManyItemSerializer
from item_detection.detection import item_detection


class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    @list_route(methods=["post"])
    def detection(self, request):

        img = request.FILES['image']
        name, score = item_detection(img)

        # 以前のItemモデルデータ削除
        pre_vm = Item.objects.all()
        pre_vm.delete()

        # Itemモデル作成
        item = Item(name=name, image=img, score=score)
        item.save()

        # シリアライズ
        serializer = ManyItemSerializer(data={'name': 'items'})

        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
