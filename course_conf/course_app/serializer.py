from .models import UserProfile, Category, SubCategory, Course, Lesson, Assignment, Certificate
from rest_framework import serializers


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'video_lesson', 'docs_lesson', 'content',]


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'


class CourseListSerializer(serializers.ModelSerializer):
    instructor = UserProfileSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_image', 'level', 'price', 'instructor' ]


class SubCategoryDetailSerializer(serializers.ModelSerializer):
    sub_category_course = CourseListSerializer(many=True, read_only=True)
    class Meta:
        model = SubCategory
        fields = ['id', 'sub_category_name', 'sub_category_course']


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name']


class CourseDetailSerializer(serializers.ModelSerializer):
    instructor = UserProfileSerializer(read_only=True)
    category = CategoryListSerializer(read_only=True)
    sub_category = SubCategoryDetailSerializer(many=True, read_only=True)
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'course_name', 'course_image', 'level',
                  'price', 'instructor' , 'category', 'sub_category',
                  'language', 'description', 'created_at', 'updated_at',
                  'lessons',]


class SubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'sub_category_name']


class CategoryDetailSerializer(serializers.ModelSerializer):
    sub_categories = SubCategoryDetailSerializer(read_only=True, many=True)
    class Meta:
        model = Category
        fields = ['category_name', 'sub_categories']



class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'