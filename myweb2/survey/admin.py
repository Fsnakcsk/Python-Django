from django.contrib import admin
from survey.models import Survey, Answer

# Admin 사이트에 반영할 내용을 기술하는 영역
class SurveyAdmin(admin.ModelAdmin):
    list_display = ('question', 'ans1', 'ans2', 'ans3', 'ans4', 'status')

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Answer)


