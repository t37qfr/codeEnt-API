from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    Object level permission to only allow owners of an object to
    edit it
    Assumes the model instance has na 'owner' attribute
    '''

    def has_object_permission(self,request,view,obj):
        '''instance must have na attribute named owner'''
        return obj.owner == request.user