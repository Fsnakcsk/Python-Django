from django.shortcuts import render
from survey.models import Survey, Answer

def main(request):
    # 설문조사 첫화면 select * from survey where status = 'y'
    # filter() 보통 10개씩 가져온다.
    survey = Survey.objects.filter(status = 'y').order_by('-survey_idx')[0]

    # objects.get(조건절) : 쿼링[ㅔ 맞는 객체 하나만 반환해준다.  ***** 반환한 겂이 없을 떄 오류남
    # objects.get() = filter.first()와 동일 , 조건에 만족하는 객체가 없을 때 Does Not Exits 에라가 발생
    # objects.all()      : objects.values(),  커리셋에 전체를 불러온다.
    # objects.filter(조건절) : 10개정도 반환해준다             ***** 오류가 안 남

    return render(request, 'survey/main.html', {'survey':survey})

def save_survey(request): # 문제에 입력한 값을 저장
    # 문제 번호와 응답번호를 Answer 객체에 저장한다.
    print(request.POST['survey_idx'])
    print(request.POST['num'])

    ans = Answer(survey_idx = request.POST['survey_idx'], num = request.POST['num'])
    ans.save() #insert 동작함

    return render(request, 'survey/success.html')

# 설계 통계를 보여줌
def show_result(request): # 결과 보여줌

    idx = request.GET['survey_idx'] # 문제 번호 가져옴
    ans = Survey.objects.get(survey_idx = idx) # select * from survey where survey_idx = 1
    answer = [ans.ans1, ans.ans2, ans.ans3, ans.ans4] # 각 문항에 대한 값을 리스트로 담는다

    # Survey.objects.raw("""SQL문 작성""") ****직접 SQL 쿼리를 담을 떄 사용하는 함수****
    surveyList = Survey.objects.raw("""
    select survey_idx, num, count(num) sum_num, round((select count(*)
                                                       from survey_answer
                                                       where survey_idx = a.survey_idx 
                                                       and num = a.num)*100/(select count(*)
                                                                            from survey_answer
                                                                            where survey_idx = a.survey_idx),1) rate
    from survey_answer a
    where survey_idx = %s
    group by survey_idx, num
    order by num
        """, idx)

    surveyList = zip(surveyList, answer)
    return render(request, 'survey/result.html', {'surveyList':surveyList})
