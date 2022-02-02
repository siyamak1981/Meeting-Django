from django import forms
from category.models import Category,SubCategory


        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ("slug",)


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        exclude = ("slug",)

     