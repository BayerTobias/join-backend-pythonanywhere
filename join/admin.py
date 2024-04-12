from django.contrib import admin
from .models import Task, Category, Subtask, CustomUser, Contact

# Register your models here.


class Task_Admin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "priority")
    list_filter = ("priority",)
    list_display_links = ("id", "title")


class Category_Admin(admin.ModelAdmin):
    list_display = ("id", "name", "color")
    list_filter = ("id",)
    list_display_links = ("id", "name", "color")


admin.site.register(Task, Task_Admin)
admin.site.register(Category, Category_Admin)
admin.site.register(Subtask)
admin.site.register(CustomUser)
admin.site.register(Contact)
