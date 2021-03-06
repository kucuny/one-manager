from django.conf.urls import url, include
from rest_framework_nested.routers import SimpleRouter, DefaultRouter, NestedSimpleRouter
from common.views import CodeSubjectViewSet

root_router = DefaultRouter()
root_router.register('subject', CodeSubjectViewSet, 'code-subject')

urlpatterns = [
    url(r'', include(root_router.urls)),
]
