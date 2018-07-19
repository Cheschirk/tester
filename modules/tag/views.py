from django.shortcuts import render


def tag_list(request):
    return render(request, '../templates/tag/tag_list.html')