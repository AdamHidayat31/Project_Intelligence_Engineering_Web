from django.shortcuts import render, get_object_or_404, redirect
from .forms import IEForm,IntExpForm,IntImpForm,KendalaForm,StatusForm,PerImpForm
from .models import IE,IntExp,IntImp,Kendala,Status,PerImp
from django.http import JsonResponse

def set_home(request):
    list_ie = IE.objects.all()
    list_intexp = IntExp.objects.all()
    list_intimp = IntImp.objects.all()
    list_kendala = Kendala.objects.all()
    list_status = Status.objects.all()
    list_perimp = PerImp.objects.all()
    context = {
        'list_ie':list_ie,
        'list_intexp':list_intexp,
        'list_intimp':list_intimp,
        'list_kendala':list_kendala,
        'list_status':list_status,
        'list_perimp':list_perimp,

    }
    return render(request, 'data_intel/Home.html',context)

def set_ie(request):
    list_ie = None
    context = None
    form = IEForm(None)
    if request.method == 'POST':
        form = IEForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
            }
            return render(request, 'data_intel/succes.html',context)
    else:
        list_ie = IE.objects.all()
        context = {
                'form':form,
                'list_ie':list_ie,
            }
        return render(request, 'data_intel/MeaningfulPage.html',context)

def delete_ie(request, id):
    dataie = get_object_or_404(IE, pk=id)
    dataie.delete()
    return redirect('data_intel:set_home')

def edit_ie(request, id):
    dataie = get_object_or_404(IE, pk=id)
    if request.method == 'POST':
        form = IEForm(request.POST, instance=dataie)
        if form.is_valid():
            form.save()
            return redirect('data_intel:set_home')
    else:
        form = IEForm(instance=dataie)
    return render(request, 'data_intel/edit_ie.html', {'form': form, 'id': id})

def set_intexp(request):
    list_intexp = None
    context = None
    form = IntExpForm(None)
    if request.method == 'POST':
        form = IntExpForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
            }
            return render(request, 'data_intel/succes.html',context)
    else:
        list_intexp = IntExp.objects.all()
        context = {
                'form':form,
                'list_intexp':list_intexp,
            }
        return render(request, 'data_intel/IntExp.html',context)
    
def delete_intexp(request, id):
    data_intexp = get_object_or_404(IntExp, pk=id)
    data_intexp.delete()
    return redirect('data_intel:set_home')

def edit_intexp(request, id):
    data_intexp = get_object_or_404(IntExp, pk=id)
    if request.method == 'POST':
        form = IntExpForm(request.POST, instance=data_intexp)
        if form.is_valid():
            form.save()
            return redirect('data_intel:set_home')
    else:
        form = IntExpForm(instance=data_intexp)
    return render(request, 'data_intel/edit_intexp.html', {'form': form, 'id': id})

def set_intimp(request):
    list_intimp = None
    context = None
    form = IntImpForm(None)
    if request.method == 'POST':
        form = IntImpForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
            }
            return render(request, 'data_intel/succes.html',context)
    else:
        list_intimp = IntImp.objects.all()
        context = {
                'form':form,
                'list_intimp':list_intimp,
            }
        return render(request, 'data_intel/IntImp.html',context)

def delete_intimp(request, id):
    data_intimp = get_object_or_404(IntImp, pk=id)
    data_intimp.delete()
    return redirect('data_intel:set_home')

def edit_intimp(request, id):
    data_intimp = get_object_or_404(IntImp, pk=id)
    if request.method == 'POST':
        form = IntImpForm(request.POST, instance=data_intimp)
        if form.is_valid():
            form.save()
            return redirect('data_intel:set_home')
    else:
        form = IntImpForm(instance=data_intimp)
    return render(request, 'data_intel/edit_intimp.html', {'form': form, 'id': id})

def set_kendala(request):
    list_kendala = None
    context = None
    form = KendalaForm(None)
    if request.method == 'POST':
        form = KendalaForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
            }
            return render(request, 'data_intel/succes.html',context)
    else:
        list_kendala = Kendala.objects.all()
        context = {
                'form':form,
                'list_kendala':list_kendala,
            }
        return render(request, 'data_intel/Kendala.html',context)

def delete_kendala(request, id):
    data_kendala = get_object_or_404(Kendala, pk=id)
    data_kendala.delete()
    return redirect('data_intel:set_home')

def edit_kendala(request, id):
    data_kendala = get_object_or_404(Kendala, pk=id)
    if request.method == 'POST':
        form = KendalaForm(request.POST, instance=data_kendala)
        if form.is_valid():
            form.save()
            return redirect('data_intel:set_home')
    else:
        form = KendalaForm(instance=data_kendala)
    return render(request, 'data_intel/edit_kendala.html', {'form': form, 'id': id})

def set_status(request):
    list_status = None
    context = None
    form = StatusForm(None)
    if request.method == 'POST':
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
            }
            return render(request, 'data_intel/succes.html',context)
    else:
        list_status = Status.objects.all()
        context = {
                'form':form,
                'list_status':list_status,
            }
        return render(request, 'data_intel/Status.html',context)

def delete_status(request, id):
    data_status = get_object_or_404(Status, pk=id)
    data_status.delete()
    return redirect('data_intel:set_home')

def edit_status(request, id):
    data_status = get_object_or_404(Status, pk=id)
    if request.method == 'POST':
        form = StatusForm(request.POST, instance=data_status)
        if form.is_valid():
            form.save()
            return redirect('data_intel:set_home')
    else:
        form = StatusForm(instance=data_status)
    return render(request, 'data_intel/edit_status.html', {'form': form, 'id': id})

def set_perimp(request):
    list_perimp = None
    context = None
    form = PerImpForm(None)
    if request.method == 'POST':
        form = PerImpForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
            }
            return render(request, 'data_intel/succes.html',context)
    else:
        list_perimp = PerImp.objects.all()
        context = {
                'form':form,
                'list_perimp':list_perimp,
            }
        return render(request, 'data_intel/PerImp.html',context)

def delete_perimp(request, id):
    data_perimp = get_object_or_404(PerImp, pk=id)
    data_perimp.delete()
    return redirect('data_intel:set_home')

def edit_perimp(request, id):
    data_perimp = get_object_or_404(PerImp, pk=id)
    if request.method == 'POST':
        form = PerImpForm(request.POST, instance=data_perimp)
        if form.is_valid():
            form.save()
            return redirect('data_intel:set_home')
    else:
        form = PerImpForm(instance=data_perimp)
    return render(request, 'data_intel/edit_perimp.html', {'form': form, 'id': id})