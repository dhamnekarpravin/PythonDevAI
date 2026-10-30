
# ==== 1. APIView =====

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Task
from .serializers import TaskSerializer


class TaskListCreateAPIView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Task, pk=pk)

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# ========== 2. Generic Views ========

# from rest_framework import generics
# from .models import Task
# from .serializers import TaskSerializer


# class TaskListCreateView(generics.ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


# class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer



# ===== 3. ViewSet ============

# from rest_framework import viewsets
# from .models import Task
# from .serializers import TaskSerializer


# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer