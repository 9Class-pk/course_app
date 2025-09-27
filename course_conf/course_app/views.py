from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.permissions import IsAuthenticated
from .permissions import IsOwner, IsStudent, IsTeacher
from .models import (UserProfile, Category, SubCategory, Course, Lesson,
                     Assignment, Certificate, Exam, Questions, Option)

from .serializer import (UserProfileSerializer, CategoryListSerializer, CategoryDetailSerializer,
                         SubCategoryListSerializer, SubCategoryDetailSerializer,
                         CourseListSerializer, CourseDetailSerializer,
                         LessonSerializer, AssignmentSerializer, CertificateSerializer,
                         ExamListSerializer, ExamDetailSerializer, QuestionsSerializer, OptionSerializer)

class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer



class UserProfileDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)


class CategoryListAPI(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryListSerializer


class CategoryDetailAPI(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryDetailSerializer


class SubCategoryListAPI(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryListSerializer


class SubCategoryDetailAPI(generics.RetrieveAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategoryDetailSerializer


class CourseListAPI(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'sub_category', 'price', 'level', 'language']
    search_fields = ["course_name"]
    ordering_fields = ["price", "created_at"]
    ordering = ["-created_at"]


class CourseDetailAPI(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['category', 'sub_category', 'price', 'level', 'language']
    search_fields = ["course_name"]
    ordering_fields = ["price", "created_at"]
    ordering = ["-created_at"]


class LessonView(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class AssignmentView(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [IsTeacher]


class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


class ExamListAPIView(generics.ListAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamListSerializer


class ExamDetailAPIView(generics.RetrieveAPIView):
    queryset = Exam.objects.all()
    serializer_class = ExamDetailSerializer


class QuestionsView(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer


class OptionView(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
