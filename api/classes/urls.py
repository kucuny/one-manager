from django.conf.urls import url, include
from rest_framework_nested.routers import SimpleRouter, DefaultRouter, NestedSimpleRouter
from classes.views import ClassesViewSet, SemesterViewSet
from classes.views import ClassesSemesterViewSet
from student.views import ClassesStudentViewSet

root_router = DefaultRouter()
root_router.register('classes', ClassesViewSet, 'classes')
root_router.register('semester', SemesterViewSet, 'semester')

classes_router = SimpleRouter()
classes_router.register('classes', ClassesViewSet, base_name='list-classes')
classes_semester_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_semester_router.register('semester', ClassesSemesterViewSet, base_name='list-classes-semester')
classes_student_router = NestedSimpleRouter(classes_router, 'classes', lookup='classes')
classes_student_router.register('student', ClassesStudentViewSet, base_name='list-classes-student')

urlpatterns = [
    url(r'', include(root_router.urls)),
    url(r'list/', include(classes_router.urls)),
    url(r'list/', include(classes_semester_router.urls)),
    url(r'list/', include(classes_student_router.urls)),
]
