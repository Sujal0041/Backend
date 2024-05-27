from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Goal
from .serializers import GoalSerializer
from django.db import models
from finance.models import Wallet, FinanceTransaction
from rest_framework.permissions import IsAuthenticated



class GoalListCreateView(generics.ListCreateAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer
    

    def post(self, request):
        try:
            data = request.data
            user = request.user
            data.update({"user": user.id})
            data.update({"remaining_amount": data["amount"]})
            serializer = GoalSerializer(data=data, context={'user': user})
            print(serializer)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)  
            import traceback
            traceback.print_exc()  
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class GoalDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer

class CalculateGoalProgress(generics.ListAPIView):
    serializer_class = None  # You can define a serializer for the response if needed

    def get_queryset(self):
        goal_id = self.kwargs['goal_id']
        try:
            queryset = Goal.objects.filter(id=goal_id)
            return queryset
        except Exception as e:
            import traceback
            traceback.print_exc()  # Print traceback for debugging
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def list(self, request, *args, **kwargs):
        try:
            goal = self.get_queryset().first()

            # Calculate the total number of months between start_date and end_date
            total_months = (goal.end_date.year - goal.start_date.year) * 12 + (goal.end_date.month - goal.start_date.month)

            # Calculate the progress based on the remaining amount and the total number of months
            progressPerMonth = round(goal.amount / total_months, 2)

            progress = 1-round(goal.remaining_amount / goal.amount, 2)

            # Update the remaining_amount field in the goal object
            # goal.remaining_amount = goal.amount - (progress * total_months)
            # goal.save()

            # Return the calculated progress
            return Response({'progress': progress})
        except Exception as e:
            import traceback
            traceback.print_exc()  # Print traceback for debugging
            return Response({"error": "An error occurred"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GoalListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GoalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GoalListViewRemoved(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter out goals where the status is "Completed"
        return Goal.objects.filter(user=self.request.user).exclude(status="Completed")

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = GoalSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   