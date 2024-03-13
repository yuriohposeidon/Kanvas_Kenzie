from rest_framework.views import APIView, status, Request, Response
from django.shortcuts import get_object_or_404


class CreateModelsMixin:

    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    

class ListModelMixin:   
    def list(self, request: Request) -> Response:
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    
class RetrieveModelMixin:
    def retrieve(self, request: Request, pk: int) -> Response:
        queryset = self.queryset
        obj = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(obj)
        return Response(serializer.data)
    
class DestroyModeMixin:
    def destroy(self, request: Request, pk: int) -> Response:
        queryset = self.queryset
        obj = get_object_or_404(queryset, pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class UpdateModelMixin:
    def partial_update(self, request: Request, pk: int) -> Response:
        obj = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)  