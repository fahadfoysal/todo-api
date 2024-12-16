from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer, TimingTodoSerializer
from .models import Todo, TimingTodo
from rest_framework.views import APIView
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


@api_view(['GET', 'POST', 'PATCH'])
def home(request):
    if request.method == 'GET':
        return Response({
            'status': 200,
            'message': 'Yes! Its working',
            'method_called': 'You called GET method'
        })
    elif request.method == 'POST':
        return Response({
            'status': 200,
            'message': 'Yes! Its working',
            'method_called': 'You called POST method'
        })
    elif request.method == 'PATCH':
        return Response({
            'status': 200,
            'message': 'Yes! Its working',
            'method_called': 'You called PATCH method'
        })
    else:
       return Response({
            'status': 400,
            'message': 'Yes! Its working',
            'method_called': 'You called INVALID method'
        }) 


@api_view(['GET'])
def get_todo(request):
    todo_objs = Todo.objects.all()
    serializer = TodoSerializer(todo_objs, many=True)
    
    return Response({
        'status': True,
        'message': 'Todo fetched',
        'data': serializer.data
    })

@api_view(['POST'])
def post_todo(request):
    try:
        data = request.data
        serializer = TodoSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'success data',
                'data': serializer.data
            })
            
        return Response({
                'status': False,
                'message': 'invalid data',
                'data': serializer.errors
            })
        
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'Something went worng'
    })
    
@api_view(['PATCH'])
def patch_todo(request):
    try:
        data = request.data
        if not data.get('uid'):
            return Response({
                'status': False,
                'message': 'uid is required',
                'data': {}
            })
            
        obj = Todo.objects.get(uid = data.get('uid'))
        serializer = TodoSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'success data',
                'data': serializer.data
            })
            
        return Response({
                'status': False,
                'message': 'invalid data',
                'data': serializer.errors
            })
        
    except Exception as e:
        print(e)
    return Response({
        'status': False,
        'message': 'invalid uid',
        'data': {}
    })
    
    
class TodoView(APIView):
    # authentication_classes = [TokenAuthentication ]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        todo_objs = Todo.objects.all()
        serializer = TodoSerializer(todo_objs, many=True)
        
        return Response({
            'status': True,
            'message': 'Todo fetched',
            'data': serializer.data
        })
         
    def post(self, request):
        try:
            data = request.data
            serializer = TodoSerializer(data = data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'success data',
                    'data': serializer.data
                })
            
            return Response({
                    'status': False,
                    'message': 'invalid data',
                    'data': serializer.errors
                })
            
        except Exception as e:
            print(e)
        return Response({
            'status': False,
            'message': 'Something went worng'
        })
        
        
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
    @action(detail=False, methods=['GET'])
    def get_timing_todo(self, request):
        objs = TimingTodo.objects.all()
        serializer = TimingTodoSerializer(objs, many=True)
        return Response({
            'status': True,
            'message': 'Timing todo fetched',
            'data': serializer.data
        })
    
    @action(detail=True, methods=['post'])
    def add_date_to_todo(self, pk, request):
        try:
            data = request.data
            serializer = TimingTodoSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': True,
                    'message': 'success data',
                    'data': serializer.data
                })
                
            return Response({
                'status': False,
                'message': 'invalid data',
                'data': serializer.errors
            })
            
        except Exception as e:
            print(e)
    
        return Response({
            'status': False,
            'message': 'Something went wrong',
        })