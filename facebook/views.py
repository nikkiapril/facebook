from django.shortcuts import render,redirect
from facebook.models import Article
from facebook.models import Trya
from facebook.models import Page
from facebook.models import Comment
from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
def play(request):
        return render(request,'play.html')

def bye(request):
        return render(request, 'bye.html')

count =0
def play2(request):

        global count
        age =16
        count = count + 1
        age = age + 5
        diary = ['오늘은 날씨가 좋았다', 'ㅇㅇ', '77']
        guest = 7
        award = '당첨입니다'
        failed = '꽝'

        if count== guest:
                result = award
        else:
                result = failed


        if age > 19:
            status = '성인'
        else:
            status = '청소년'



        return render(request, 'play2.html', {'cnt': count, 'age': status, 'diary': diary,
                                              'guest':guest,'award':award,'result':result})


def multiple(request):

        num1 = 21
        num2 = 22

        mulofSev1 = num1%7
        mulofSev2 = num2%7

        answer = '7의 배수 입니다'
        wrong = '7의 배수가 아닙니다.'

        if mulofSev1 == 0:
                test = answer
        else:
                test = wrong

        if mulofSev2 == 0:
                result = answer
        else:
                result = wrong



        return render(request, 'multiple.html' ,{'result':result, 'mulofSev1':mulofSev1,
                                                 'mulofSev2':mulofSev2, 'answer':answer, 'wrong':wrong, 'num1':num1,'num2':num2,'test':test})


def profile(request):
          return render(request, 'profile.html')

def tryrr(request):
         return render(request, 'tryrr.html')

def fail(request):
         return render(request, 'fail.html')


def help(request):
         return render(request, 'help.html')


def warn(request):
         return render(request, 'warn.html')


# 나만의복습
def trynewsfeed(request):
         trya = Trya.objects.all() #장고에서 모든 아티클을 가져와라
         return render(request, 'trynewsfeed.html' , {'trya': trya})

# 페이스북 본격적으로 시작~!

# 메인-뉴스피드

def main(request):
    return render(request, 'main.html')

def bora(request):
    return render(request, 'aboutme.html')

def newsfeed(request):

        articles = Article.objects.order_by('-created_at')
        if request.method == 'POST':  # 폼이 전송되었을 때만 아래 코드를 실행
            new_article = Article.objects.create(
                author=request.POST['author'],
                title=request.POST['title'],
                text=request.POST['content'],
                password=request.POST['password']
            )
            return redirect('/main')
            # 새글 등록 끝

        return render(request, 'newsfeed.html', {'articles': articles})



# 좋아요 버튼구현
def like_button(request,pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        #article.like += 1
        Article.objects.create(
            like=request.POST.get('like')
        )
        article.like +1


    return render(request, 'newsfeed.html', {'articles': article})

#상세보기 페이지
def detail_feed(request, pk):
    article = Article.objects.get(pk=pk) #프라이머리키값 만 들고
    if request.method == 'POST':
        Comment.objects.create(
            article=article,
            author=request.POST.get('nickname'),
            text=request.POST.get('reply'),
            password=request.POST.get('password')

        )
        return redirect(f'/feed/{article.pk}')
        #return redirect('/')


    return render(request, 'detail_feed.html', {'feed': article})

#글쓰기?!
def new_feed(request):
    if request.method == 'POST': # 폼이 전송되었을 때만 아래 코드를 실행
        new_article = Article.objects.create(
            author=request.POST['author'],
            title=request.POST['title'],
            text=request.POST['content'],
            password=request.POST['password']
        )
        return redirect('/main')
        # 새글 등록 끝

    return render(request, 'new_feed.html')

# 삭제페이지
def remove_feed(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method =='POST':
         if request.POST['password'] == article.password:
             article.delete()
             return redirect('/main')
         else:
             return redirect('/fail/')
    return  render(request, 'remove_feed.html',{'feed':article})

# 코멘트 삭제 페이지
def remove_comment(request, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method=='POST':
        if request.POST['password'] == comment.password:
            comment.delete()
            return redirect('/main')
        else:
            return redirect('/fail/')
    return  render(request, 'remove_comment.html',{'comment':comment})

# 오류메세지 페이지
def fail(request):

    return render(request, 'fail.html')


# 수정페이지
def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if request.POST['password'] == article.password:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect('/main')
        else:
            return redirect('/fail/')
            #return redirect(f'/feed/{article.pk}')


    return render(request, 'edit_feed.html', {'feed': article})

# 코멘트 수정페이지
def edit_comment(request, pk):

    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        if request.POST['password'] == comment.password:
            comment.author = request.POST['author']
            comment.text = request.POST['content']
            comment.save()
            return redirect('/main')
        else:
            return redirect('/fail/')

    return render(request, 'edit_comment.html', {'feed': comment})

def new_page(request):
    if request.method == 'POST':
        new_page = Page.objects.create(
            master=request.POST['master'],
            name=request.POST['name'],
            text=request.POST['text'],
            category=request.POST['category']
        )
        return redirect('/pages/')

    return render(request, 'new_page.html')

# 뉴피드
def pages(request):
    pages = Page.objects.all()
    return render(request, 'page_list.html', {'pages': pages})

#수정하기/ 삭제하기
def edit(request):
    return render(request, 'edit.html')

def remove(request):
    return render(request, 'remove.html')

# 서치/ 검색기능


def search_list(request, author):

    article_list = Article.objects.filter(author=author)


    return render(request, 'newsfeed.html', { 'articles': list(article_list)})


@require_POST# 해당 뷰는 POST method 만 받는다.
#@csrf_exempt
def post_like(request):
    if request.method == 'POST' and request.is_ajax():
        pk = request.POST['pk']
        status = request.POST['status']

        if status == '0':
            articles = Article.objects.get(pk=pk)
            if articles.total_like != '':
                articles.total_like = int(articles.total_like) + 1
                articles.save()
            else:
                articles.total_like = 1
                articles.save()
        else:
            articles = Article.objects.get(pk=pk)
            if articles.total_like != '':
                articles.total_like = int(articles.total_like) - 1
                articles.save()
            else:
                articles.total_like = 0
                articles.save()

        return HttpResponse(json.dumps({"article_like":articles.total_like, "status":status}), content_type="application/json")
    else :
        articles = Article.objects.all()

        return render(request, 'newsfeed.html', {'articles': articles})

@require_POST
#@csrf_exempt
def comment_write(request):
    if request.method == 'POST' and request.is_ajax():
        name = request.POST['name']
        password = request.POST['password']
        content = request.POST['content']
        article = request.POST['article']

        # 게시글번호로 Article 꺼내기
        articles = Article.objects.get(pk=article)

        # 위에서꺼낸 Article과 html에서 전달받은정보로 insert
        Comment.objects.create(
            article=articles,
            author=name,
            text=content,
            password=password
        )

        # 방금 insert된 생성날짜 꺼내기
        created_at = Comment.objects.latest('id').created_at

        # 방금 insert된 코멘트의 pk
        new_comment = Comment.objects.latest('id').id

        # 저장된 데이터 html에서 보여주기위해 리턴
        test = {
            "name":name,
            "password":password,
            "content":content,
            "article":new_comment,
            "created_at":created_at.strftime("%Y-%m-%d %I:%M %p")
            # 표현법=> %Y:4자리 년도, %m:2자리 월, %d:2자리 일(1월은 01로), %I: 12시간, %H: 24시간, %M:분, %p:오전/오후
            }
        return HttpResponse(json.dumps(test), content_type="application/json")

    else :
        articles = Article.objects.all()
        if request.method == 'POST':
            Comment.objects.create(
                article=articles,
                author=request.POST.get('nickname'),
                text=request.POST.get('reply'),
                password=request.POST.get('password')

            )
        return HttpResponse(json.dumps({'articles': articles}), content_type="application/json")
        #return render(request, 'newsfeed.html', {'articles': articles})