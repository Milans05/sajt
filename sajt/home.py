from django.shortcuts import render


def homepage(request):
    return render(request, 'index.html')


def number(request):

    mojtekst = request.GET['textic']

    mojsplit = mojtekst.split()
    prazan = {}

    for text in mojsplit:
        if text in prazan:
            prazan[text] += 1
        else:
            prazan[text] = 1
    sortiranje = sorted(prazan.items(), key= lambda s: s[1], reverse=True)
    print("Najvise ponovnjena rec je ", sortiranje[0])
    return render(request, 'brojac.html', {'showtext': sortiranje})



