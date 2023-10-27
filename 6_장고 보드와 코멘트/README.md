## 오늘 만난 오류 횟수 : 11번

#### 주요 오류들
- Not NULL constraint failed
- NoReverseMatch at
- IntegrityError at
- HTTP ERROR 405

대부분 URL 실수였다... 

## 어려웠던 점
회원가입, 로그인/로그아웃은 순식간에 끝냈지만 이번주 수업내용은 한페이지당 한시간씩 쓴 것 같다
N:M을 다룰 때 변수명이나 DB에 접근하는 법을 헷갈렸다.
특히 외래키나 역참조 이름을 못찾아서 헤맸다.
이번주 복습이 중요할 것 같다.
css 까먹었다

## 잊으면 슬퍼질 것들 ...
profile.html 작성법 ...

```
def comment(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.board = board
            comment.author = request.user
            comment.save()
            return redirect('boards:detail', board.pk)


def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.author:
        comment.delete()
        return redirect('boards:detail', board_pk)
```