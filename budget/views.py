from django.shortcuts import render
from budget.models import Budget
from budget.serializers import BudgetSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.


# Views
class BudgetListCreateView(generics.ListCreateAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer


# Helper functions to retrieve queryset and serialize it.
def get_queryset(request):
    queryset = Budget.objects.all()
    return queryset


def get_serialized_data(queryset):
    serializer = BudgetSerializer(queryset, many=True)
    return serializer.data


# Views using helper functions
class BudgetListView(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        queryset = get_queryset(request)
        serialized_data = get_serialized_data(queryset)
        return Response(serialized_data, status=status.HTTP_200_OK)


class BudgetDetailView(generics.RetrieveUpdateDestroyAPIView):
    def get(self, request, *args, **kwargs):
        queryset = get_queryset(request)
        obj = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = BudgetSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        queryset = get_queryset(request)
        obj = get_object_or_404(queryset, pk=kwargs['pk'])
        serializer = BudgetSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        queryset = get_queryset(request)
        obj = get_object_or_404(queryset, pk=kwargs['pk'])
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

