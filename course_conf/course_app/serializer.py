from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from .models import (UserProfile, Category, SubCategory, Course,
                     Lesson, Assignment, Certificate, Exam,
                     Questions, Option, Comment, Cart, CartItem )



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirm = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=UserProfile.ROLE_CHOICES)

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'password_confirm',
                  'first_name', 'last_name', 'role')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')
        user = UserProfile.objects.create_user(**validated_data)
        return user


class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(read_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = UserProfile.objects.get(email=email)
        except UserProfile.DoesNotExist:
            raise serializers.ValidationError("User with this email does not exist.")

        user = authenticate(username=user.username, password=password)
        if not user:
            raise serializers.ValidationError("Invalid credentials.")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        refresh = RefreshToken.for_user(user)
        attrs['access'] = str(refresh.access_token)
        attrs['refresh'] = str(refresh)
        return attrs


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
        fields = ['option_title', 'answer', ]


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


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = '__all__'