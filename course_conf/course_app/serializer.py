from .models import (UserProfile, Category, SubCategory, Course,
                     Lesson, Assignment, Certificate, Exam,
                     Questions, Option, )
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
        fields = ['id', 'title', 'description', 'due_date', 'lesson', 'students']


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


class ExamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exam
        fields = ['id', 'exam_name',]


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = ['id', 'option_title', 'answer', 'questions']


class QuestionsSerializer(serializers.ModelSerializer):
    options0 = OptionSerializer(many=True, read_only=True)

    class Meta:
        model = Questions
        fields = ['id', 'question_title', 'passing_score',  'options0' ]


class ExamDetailSerializer(serializers.ModelSerializer):
    questions0 = QuestionsSerializer(many=True, read_only=True)

    class Meta:
        model = Exam
        fields = ['exam_name', 'duration', 'questions0',]



