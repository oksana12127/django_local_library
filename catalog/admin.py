from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language, DateWriting

# admin.site.register(Book)
# admin.site.register(Author)
# admin.site.register(Genre)


# admin.site.register(BookInstance)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    # model = Book


class BookInline(admin.TabularInline):
    # model = BookInstance

    model = Book





# Define the admin class


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'last_name'), ('date_of_birth', 'date_of_death')]
    inlines = [BookInline]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    # list_display = ('langauge_book')
    fields = ['langauge_book']


@admin.register(DateWriting)
class DateWritingAdmin(admin.ModelAdmin):
    # list_display = ('langauge_book')
    fields = ['date_book']


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # list_display = ('langauge_book')
    # fields = ['genre']
    pass

# Register the admin class with the associated model
# admin.site.register(Author, AuthorAdmin)


# Register the Admin classes for Book using the decorator

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'language')
    inlines = [BooksInstanceInline]


# Register the Admin classes for BookInstance using the decorator


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    # inlines = [BooksInstanceInline]
    # fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    list_filter = ('status', 'due_back')

    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),
    )
    # inlines = [BooksInstanceInline]
