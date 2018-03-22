from django.db.models import Q
#generic views
from rest_framework import generics,mixins
from postings.models import BlogPost
from .serialisers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly




'''Create'''
class BlogPostAPIListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

    def get_serializer_context(self,*args,**kwargs):
        return {'request':self.request}


'''Create'''
class BlogPostAPIView(mixins.CreateModelMixin,generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    #queryset = BlogPost.objects.all()

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
        return qs

    #add the actual user to the query
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

    #if ad a http method it become avaible
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

    def get_serializer_context(self,*args,**kwargs):
        return {'request':self.request}

'''CRUD - C: '''
class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrReadOnly,]
    #queryset = BlogPost.objects.all()

    def get_queryset(self):
        return BlogPost.objects.all()

    def get_serializer_context(self,*args,**kwargs):
        return {'request':self.request}

