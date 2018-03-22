from rest_framework import serializers
from postings.models import BlogPost


'''
Serializer do 2 things:
1. convert to JSON
2. validation for data passed
'''
class BlogPostSerializer(serializers.ModelSerializer):
    '''For API reverse'''
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['uri','pk','user','title','content','timestamp']
        read_only_fields = ['pk','user']

    '''Add URI to the response list'''
    def get_uri(self,obj):
        request = self.context.get('request')
        return obj.get_api_url(request=request)


    '''validation function for the title field'''
    def validate_title(self,value):
        #this include the post itself
        qs = BlogPost.objects.filter(title__iexact=value)
        #exclude one
        print(self.instance)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise serializers.ValidationError('The title must be unique')
        return value