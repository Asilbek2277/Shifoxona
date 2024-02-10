from django.shortcuts import render, redirect

from .models import *


#Xona jadvalining viewlari

def hamma_xona(request):
    if request.method=="POST":
        Xona.objects.create(
            number=request.POST.get('number'),
            band=request.POST.get('band', False)=='on',
            joy=request.POST.get('joy')
        )
        return redirect('/hamma_xona/')



    xona_raqami=request.GET.get('xona_raqami')

    natija=Xona.objects.all()
    if xona_raqami is not None:
        natija=Xona.objects.filter(number__contains=xona_raqami)

    context={
        'xonalar': natija
    }
    return render(request, 'hamma_xona.html', context)

def xona_ochirish(request, pk):
    Xona.objects.get(id=pk).delete()
    return redirect('/hamma_xona/')



def xona_tahrirlash(request, pk):
        if request.method=='POST':
            xonalar=Xona.objects.get(id=pk)
            xonalar.number=request.POST.get('number')
            xonalar.band=request.POST.get('band', False)=='on'
            xonalar.joy=request.POST.get('joy')
            xonalar.save()

            return redirect('/hamma_xona/')

        context={
            'xonalar':Xona.objects.get(id=pk)
        }

        return render(request, 'xona_tahrirlash.html', context)





#Xizmat jadvalining hamma viewlari

def hamma_xizmatlar(request):
    if request.method=="POST":
        Xizmat.objects.create(
            nom=request.POST.get('nom'),
            xona=Xona.objects.get(id=request.POST.get('xona')) ,
            narx=request.POST.get('narx')
        )
        return redirect('/hamma_xizmatlar/')



    xizmat_nomi=request.GET.get('xizmat_nomi')

    natija=Xizmat.objects.all()
    if xizmat_nomi is not None:
        natija=Xizmat.objects.filter(nom__contains=xizmat_nomi)

    context={
        'xizmatlar': natija,
        'xona':Xona.objects.all()
    }
    return render(request, 'hamma_xizmatlar.html', context)

def xizmat_ochirish(request, pk):
    Xizmat.objects.get(id=pk).delete()
    return redirect('/hamma_xizmatlar/')



def xizmat_tahrirlash(request, pk):
        if request.method=='POST':
            xizmat=Xizmat.objects.get(id=pk)

            xizmat.nom=request.POST.get('nom')
            xizmat.xona=Xona.objects.get(id=request.POST.get('xona'))
            xizmat.narx=request.POST.get('narx')
            xizmat.save()

            return redirect('/hamma_xizmatlar/')

        context={
            'xizmat':Xizmat.objects.get(id=pk),
            'xona': Xona.objects.all()
        }

        return render(request, 'xizmat_tahrirlash.html', context)


#Shifokor jadvalining barcha view lari


def hamma_shifokor(request):
    if request.method=='POST':
        Shifokor.objects.create(
            ism=request.POST.get('ism'),
            ish_vaqti=request.POST.get('ish_vaqti'),
            tel=request.POST.get('tel'),
            xizmat=Xizmat.objects.get(id=request.POST.get('xizmat'))
        )
        return redirect('/hamma_shifokor/')

    shifokor_ismi = request.GET.get('shifokor_ismi')

    natija = Shifokor.objects.all()
    if shifokor_ismi is not None:
        natija = Shifokor.objects.filter(ism__contains=shifokor_ismi)


    context ={
        'shifokor': natija,
        'xizmat': Xizmat.objects.all()
    }

    return render(request, 'hamma_shifokor.html',context)



def shifokor_ochirish(request, pk):
    Shifokor.objects.get(id=pk).delete()
    return redirect('/hamma_shifokor/')



def shifokor_tahrirlash(request, pk):
        if request.method=='POST':
            shifokor=Shifokor.objects.get(id=pk)

            shifokor.ism=request.POST.get('ism')
            shifokor.ish_vaqti=request.POST.get('ish_vaqti')
            shifokor.tel=request.POST.get('tel')
            shifokor.xizmat=Xizmat.objects.get(id=request.POST.get('xizmat'))
            shifokor.save()

            return redirect('/hamma_shifokor/')

        context={
            'shifokor':Shifokor.objects.get(id=pk),
            'xizmat': Xizmat.objects.all()
        }

        return render(request, 'shifokor_tahrirlash.html', context)


#   Buyurtma jadvalining hamma viewlari

def hamma_buyurtma(request):
    if request.method=='POST':
        Buyurtma.objects.create(
            sana=request.POST.get('sana'),
            tashhis=request.POST.get('tashhis'),
            xona=Xona.objects.get(id=request.POST.get('xona')),
            shifokor=Shifokor.objects.get(id=request.POST.get('shifokor')),
            kishi_soni=request.POST.get('kishi_soni'),
            summa=request.POST.get('summa'),
            tuzaldi=request.POST.get('tuzaldi', False)=='on'
        )
        return redirect('/hamma_buyurtma/')

    buyurtma = request.GET.get('buyurtma')

    natija = Buyurtma.objects.all()
    if buyurtma is not None:
        natija = Buyurtma.objects.filter(tashhis__contains=buyurtma)


    context ={
        'buyurtma': natija,
        'xona': Xona.objects.all(),
        'shifokor': Shifokor.objects.all()
    }

    return render(request, 'hamma_buyurtma.html',context)



def buyurtma_ochirish(request, pk):
    Buyurtma.objects.get(id=pk).delete()
    return redirect('/hamma_buyurtma/')



def buyurtma_tahrirlash(request, pk):
        if request.method=='POST':
            buyurtma=Buyurtma.objects.get(id=pk)

            buyurtma.sana=request.POST.get('sana')
            buyurtma.tashhis=request.POST.get('tashhis')
            buyurtma.xona=Xona.objects.get(id=request.POST.get('xona'))
            buyurtma.shifokor=Shifokor.objects.get(id=request.POST.get('shifokor'))
            buyurtma.kishi_soni = request.POST.get('kishi_soni')
            buyurtma.summa = request.POST.get('summa')
            buyurtma.tuzaldi = request.POST.get('tuzaldi', False) == 'on'
            buyurtma.save()

            return redirect('/hamma_buyurtma/')

        context={
            'buyurtma':Buyurtma.objects.get(id=pk),
            'xona': Xona.objects.all(),
            'shifokor':Shifokor.objects.all()
        }

        return render(request, 'buyurtma_tahrirlash.html', context)


# Bemor jadvalining hamma viewlari



def hamma_bemorlar(request):
    if request.method=='POST':
        Bemor.objects.create(
            ism=request.POST.get('ism'),
            tel=request.POST.get('tel'),
            buyurtma=Buyurtma.objects.get(id=request.POST.get('buyurtma'))
        )
        return redirect('/hamma_bemorlar/')

    bemor_ism = request.GET.get('bemor_ism')

    natija = Bemor.objects.all()
    if bemor_ism is not None:
        natija = Bemor.objects.filter(ism__contains=bemor_ism)


    context ={
        'bemor': natija,
        'buyurtma': Buyurtma.objects.all()
    }

    return render(request, 'hamma_bemorlar.html',context)



def bemor_ochirish(request, pk):
    Bemor.objects.get(id=pk).delete()
    return redirect('/hamma_bemorlar/')



def bemor_tahrirlash(request, pk):
        if request.method=='POST':
            bemor=Bemor.objects.get(id=pk)

            bemor.ism=request.POST.get('ism')
            bemor.tel=request.POST.get('tel')
            bemor.buyurtma=Buyurtma.objects.get(id=request.POST.get('buyurtma'))
            bemor.save()

            return redirect('/hamma_bemorlar/')

        context={
            'bemor':Bemor.objects.get(id=pk),
            'buyurtma': Buyurtma.objects.all()
        }

        return render(request, 'bemor_tahrirlash.html', context)
