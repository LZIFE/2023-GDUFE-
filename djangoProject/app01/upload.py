from django.shortcuts import render


def upload(request):
    return render(request, 'scholarship_review.html')
