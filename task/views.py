from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Task, TestTask, UserSolution
from .serializers import TaskSerializer, TodecideSerializer
from django.http import JsonResponse

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TodecideView(APIView):
    def post(self, request, task_id):
        serializer = TodecideSerializer(data = request.data)
        if serializer.is_valid():
            task = Task.objects.get(id = task_id)
            begin_of_code = task.first_text
            part_solution = serializer.validated_data['solution']
            solution = begin_of_code + part_solution
            user_function = exec(solution, globals())

            tests = TestTask.objects.filter(task = task)
            all_test = list()
            t = list()

            for elem in tests:
                var = elem.test_var
                var_list = var.split()
                all_test.append(var_list)
                t.append(elem.result)

            test_results = [eval(element) for element in t]

            res_list = []
            for item in all_test:
                modified_item = [eval(element) for element in item]
                res_list.append(modified_item)

            mu = task.name_function
            user_function_tu = globals().get(mu)

            user_test_result = list()
            for elem in res_list:
                code_result = user_function_tu(*elem)
                user_test_result.append(code_result)


            count_same_elements = sum(1 for a, b in zip(user_test_result, test_results) if a == b)
            # UserSolution.objects.create(solution=solution, user=request.user, count_succes = count_same_elements)
            to_return_list = list(zip(test_results, user_test_result))
            my_string = '; '.join(f'Expected {expected}, received {received}' for expected, received in to_return_list)
            data = {'message': f'{my_string}'}
            return JsonResponse(data)





            
            







