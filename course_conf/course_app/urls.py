from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (UserProfileDetailAPIView, UserProfileListAPIView,
                    CategoryListAPI, CategoryDetailAPI,
                    SubCategoryListAPI, SubCategoryDetailAPI, CourseListAPI,
                    CourseDetailAPI, LessonView, AssignmentView, CertificateView,
                    ExamListAPIView, ExamDetailAPIView, QuestionsView, OptionView)


router = DefaultRouter()
router.register('lessons', LessonView)
router.register('assignments', AssignmentView)
router.register('certificates', CertificateView)
router.register('questions', QuestionsView)
router.register('options', OptionView)




urlpatterns = [

    path('categories/', CategoryListAPI.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailAPI.as_view(), name='category_detail'),
    path('sub_categories/', SubCategoryListAPI.as_view(), name='subcategory_list'),
    path('sub_categories/<int:pk>/', SubCategoryDetailAPI.as_view(), name='subcategory_detail'),
    path('courses/', CourseListAPI.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailAPI.as_view(), name='course_detail'),
    path('exam/', ExamListAPIView.as_view(), name='exam_list'),
    path('exam/<int:pk>/', ExamDetailAPIView.as_view(), name='exam_detail'),
    path('users/', UserProfileListAPIView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail'),
    path('', include(router.urls)),
]