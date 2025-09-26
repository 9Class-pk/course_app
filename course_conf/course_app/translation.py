from .models import (Category, SubCategory, Course, Lesson,
                     Assignment, Certificate, Questions,
                     Exam, Option)
from modeltranslation.translator import TranslationOptions,register

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('category_name',)

@register(SubCategory)
class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('sub_category_name', )

@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ('course_name', 'description',)

@register(Lesson)
class LessonTranslationOptions(TranslationOptions):
    fields = ['title', 'content']

@register(Assignment)
class AssignmentTranslationOptions(TranslationOptions):
    fields = ['title', 'description']

@register(Exam)
class ExamTranslationOptions(TranslationOptions):
    fields = ['exam_name']

@register(Questions)
class QuestionsTranslationOptions(TranslationOptions):
    fields = ['question_title',]

@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ['option_title',]
