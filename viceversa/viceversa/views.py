from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    words = user_text.lower().split()
    words_count = len(words)
    return render(request, 'reverse.html', {'usertext': user_text, 'reversedtext': reversed_text,
                                            'words_count': words_count})
