from django.contrib import admin
import nested_admin


from .models import (UserProfile, Category, SubCategory, Course, Lesson,
                     Assignment, Certificate, Questions, Option, Exam,
                     Cart, CartItem, Comment)

from modeltranslation.admin import (TranslationAdmin, TranslationInlineModelAdmin,
                                   TranslationTabularInline, TranslationBaseModelAdmin)




admin.site.register(UserProfile)
admin.site.register(Certificate)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Comment)





class BaseTranslationAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }



class SubCategoryInline(TranslationTabularInline):
    model = SubCategory
    extra = 1


@admin.register(Category)
class CategoryAdmin(BaseTranslationAdmin):
    inlines = [SubCategoryInline]


class AssignmentInline(TranslationTabularInline, nested_admin.NestedStackedInline):
    model = Assignment
    extra = 1


class LessonInline(TranslationTabularInline, nested_admin.NestedStackedInline):
    model = Lesson
    extra = 1
    inlines = [AssignmentInline]


@admin.register(Course)
class CourseAdmin(nested_admin.NestedModelAdmin, BaseTranslationAdmin):

    inlines = [LessonInline]



#2222

class OptionInline(nested_admin.NestedModelAdmin):
    model = Option
    extra = 1

class QuestionsInline(TranslationTabularInline):
    model = Questions
    extra = 1
    inlines = [OptionInline]



@admin.register(Exam)
class ExamAdmin(BaseTranslationAdmin,):

    inlines = [QuestionsInline]

