from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from multiselectfield import MultiSelectField



class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('student', 'student'),
        ('teacher', 'teacher')
    )
    role = models.CharField(max_length=32, choices=ROLE_CHOICES, default='student')
    profile_picture = models.ImageField(upload_to='user_images')
    bio = models.TextField()
    phone_number = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name}, {self.last_name}, {self.role}'


class Category(models.Model):
    category_name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.category_name


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='sub_categories')
    sub_category_name = models.CharField(max_length=64, unique=True,)

    def __str__(self):
        return f'{self.category}, {self.sub_category_name}'


class Course(models.Model):
    course_name = models.CharField(max_length=64)
    course_image = models.ImageField(upload_to='course_images')
    course_video = models.FileField(upload_to='course_videos')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ManyToManyField(SubCategory, related_name='sub_category_course')
    description = models.TextField()
    LEVEL_CHOICES = (
    ('beginner ' , 'beginner'),
    ('middle', 'middle'),
    ('advanced', 'advanced')
    )
    level = MultiSelectField(max_length=32, choices=LEVEL_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    LANGUAGE_CHOICES = (
        ('russian', 'russian'),
        ('english ', 'english'),
        ('kyrgyz', 'kyrgyz'),
        ('german', 'german'),
        ('france', 'france'),
    )
    language = MultiSelectField(max_length=32, choices=LANGUAGE_CHOICES, default='russian',
                                min_choices=1, max_choices=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='instructors')

    def __str__(self):
        return self.course_name

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')
    title = models.CharField(max_length=100)
    video_lesson = models.FileField(upload_to='lesson_videos')
    docs_lesson = models.FileField(upload_to='lesson_docs')
    content = models.TextField(null=True, blank=True    )

    def __str__(self):
        return f'{self.course}, {self.title}'


class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    students = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.lesson}, {self.title}'


class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=32)
    duration = models.DurationField()

    def __str__(self):
        return f'{self.course}, {self.exam_name}'


class Questions(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='questions0')
    question_title = models.CharField(max_length=50)
    passing_score = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.exam}, {self.question_title}'


class Option(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE, related_name='options0', null=True,
        blank=True)
    option_title = models.CharField(max_length=100)
    answer = models.BooleanField()

    def __str__(self):
        return f'{self.question}, {self.option_title}'


class Certificate(models.Model):
    student = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    issued_at = models.DateField(auto_now_add=True)
    certificate_url = models.FileField(upload_to='certificates')

    def __str__(self):
        return f'{self.course},{self.student}'


class Comment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    test = models.TextField()
    stars = models.IntegerField(choices=[(i, str(i))for i in range(1, 6)])
    created_date =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.course}, {self.course}'


class Cart(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.cart.user}, {self.course}'