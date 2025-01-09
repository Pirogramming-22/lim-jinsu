from django.shortcuts import render, redirect, get_object_or_404
from .models import Review


def home(request):
    reviews = Review.objects.all()  # 모든 리뷰 데이터 가져오기
    context = {'reviews': reviews}
    return render(request, 'reviews/reviews_list.html',context)

def detail(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    context = {
        'title': review.title,
        'year': review.year,
        'genre': review.genre,
        'director': review.director,
        'cast': review.cast,
        'rating': review.rating,
        'runtime': review.runtime,
        'review': review,  
        'review_id': review.id,
    }
    return render(request, 'reviews/reviews_detail.html', context)


def create(request):
    if request.method == 'POST':
        # 데이터 저장
        title = request.POST.get('title')  # 폼 데이터 가져오기
        year = request.POST.get('year')
        genre = request.POST.get('genre')
        director = request.POST.get('director')
        cast = request.POST.get('cast')
        rating = request.POST.get('rating')
        runtime = request.POST.get('runtime')
        review_text = request.POST.get('review')

        # 데이터베이스 저장
        Review.objects.create(
            title=title,
            year=int(year),
            genre=genre,
            director=director,
            cast=cast,
            rating=float(rating),
            runtime=int(runtime),
            review=review_text
        )
        return redirect('home')  # 저장 후 홈 페이지로 리디렉션

    return render(request, 'reviews/review_form.html')  # 작성 폼 렌더링

def update(request, review_id):
    # ID에 해당하는 리뷰 데이터 가져오기
    review = get_object_or_404(Review, id=review_id)

    if request.method == 'POST':
        # 수정된 데이터 저장
        review.title = request.POST['title']
        review.year = request.POST['year']
        review.genre = request.POST['genre']
        review.director = request.POST['director']
        review.cast = request.POST['cast']
        review.rating = request.POST['rating']
        review.runtime = request.POST['runtime']
        review.review = request.POST['review']
        review.save()  # 데이터베이스에 저장
        return redirect('detail', review_id=review.id)  # 디테일 페이지로 리디렉션(돌아가기)

    # GET 요청 시 기존 데이터 전달
    context = {
        'review': review,
    }
    return render(request, 'reviews/review_form.html', context)

def delete(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()  # 리뷰 삭제
    return redirect('home')  # 삭제 후 리스트 페이지로 리디렉션