from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Tag, Scope


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        is_article = False
        is_main_bool_count = int()
        for form in self.forms:
            try:
                if str(form.cleaned_data['is_main']) == 'True':
                    is_main_bool_count += 1
                else:
                    pass
                if form.cleaned_data['id']:
                    is_article = True
                else:
                    pass
            except KeyError:
                pass
        if is_main_bool_count == 1:
            pass
        elif is_main_bool_count > 1 and is_article is True:
            raise ValidationError('Параметр Основной должен быть заполнен не более одного раза')
        elif is_main_bool_count < 1:
            raise ValidationError('Параметр Основной должен быть обязательно указан')
        # elif is_article is True:
        #     raise ValidationError('Параметр Основной не заполнен')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset
    extra = 0


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
