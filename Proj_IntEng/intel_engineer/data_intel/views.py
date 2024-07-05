from django.shortcuts import render, get_object_or_404, redirect
from .forms import *
from .models import *
from django.http import JsonResponse
import requests
from rest_framework import generics
from .serializers import *

def set_home(request):
    list_dataprojek = DataProjek.objects.all()
    context = None
    form = DataProjekForm(None)
    namap = None
    if request.method == 'POST':
        form = DataProjekForm(request.POST)
        if form.is_valid():
            namap = form.cleaned_data['nama_proyek']
            request.session['nama_proyek'] = namap
            request.session.modified = True
            form.save()
            list_dataprojek = DataProjek.objects.all()
            namap = request.session['nama_proyek']
            context = {
                'form':form,
                'list_dataprojek':list_dataprojek,
                'namap':namap,
            }
            return render(request, 'data_intel/Home.html', context)
    else:
        list_dataprojek = DataProjek.objects.all()
        context = {
            'form':form,
            'list_dataprojek':list_dataprojek,
            'namap':namap,
        }
        return render(request, 'data_intel/Home.html', context)
    
def set_projek_session(request, id):
    try:
        projek = DataProjek.objects.get(pk=id)
        request.session['nama_proyek'] = projek.nama_proyek
        request.session.modified = True
        return redirect('data_intel:set_home')
    except DataProjek.DoesNotExist:
        return JsonResponse({'error': 'proyek tidak ditemukan'}, status=404)

def get_projek_detail(request, id):
    try:
        projek = DataProjek.objects.get(pk=id)
        nama_p = projek.nama_proyek
        list_ie = IE.objects.filter(projek=projek)
        list_intexp = IntExp.objects.filter(projek=projek)
        list_intimp = IntImp.objects.filter(projek=projek)
        list_kendala = Kendala.objects.filter(projek=projek).order_by('-id')
        list_status = Status.objects.filter(projek=projek).order_by('-id')
        list_perimp = PerImp.objects.filter(projek=projek)

        context = {
            'nama_p': nama_p,
            'projek': projek,
            'list_ie': list_ie,
            'list_intexp': list_intexp,
            'list_intimp': list_intimp,
            'list_kendala': list_kendala,
            'list_status': list_status,
            'list_perimp': list_perimp,
        }
        return render(request, 'data_intel/projek_detail.html', context=context)
    except DataProjek.DoesNotExist:
        return JsonResponse({'error': 'proyek tidak ditemukan'}, status=404)


def set_ie(request):
    context = None
    form = IEForm(None)
    if request.session.get('nama_proyek', None):
        nama_p = request.session.get('nama_proyek', None)
        nprojek = DataProjek.objects.get(nama_proyek=nama_p)
        initial_data = {'projek': nprojek}

        try:
            ie_instance = IE.objects.get(projek=nprojek)
            # If the data already exists, show the "data sudah tersedia" page
            context = {
                'ie_instance': ie_instance,
                'nama_p': nama_p,
            }
            return render(request, 'data_intel/DataTersediaM.html', context)
        except IE.DoesNotExist:
            ie_instance = None

        if request.method == 'POST':
            form = IEForm(request.POST, instance=ie_instance)
            if form.is_valid():
                ie = form.save(commit=False)
                ie.projek = nprojek  # Set projek to the current project
                ie.save()
                context = {
                    'form': form,
                    'nama_p': nama_p,
                }
                return render(request, 'data_intel/succes.html', context)
        else:
            form = IEForm(initial=initial_data)
            context = {
                'form': form,
                'nama_p': nama_p,
                'nprojek': nprojek,
            }
        return render(request, 'data_intel/IE.html', context)

    return render(request, 'data_intel/IE.html', {'form': form, 'nama_p': request.session.get('nama_proyek', None)})




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
    context = None
    form = IntExpForm(None)
    if request.session.get('nama_proyek', None):
        nama_p = request.session.get('nama_proyek', None)
        nprojek = DataProjek.objects.get(nama_proyek=nama_p)
        initial_data = {'projek': nprojek}

        try:
            intexp_instance = IntExp.objects.get(projek=nprojek)
            # If the data already exists, show the "data sudah tersedia" page
            context = {
                'intexp_instance': intexp_instance,
                'nama_p': nama_p,
            }
            return render(request, 'data_intel/DataTersediaExp.html', context)
        except IntExp.DoesNotExist:
            intexp_instance = None

        if request.method == 'POST':
            form = IntExpForm(request.POST, instance=intexp_instance)
            if form.is_valid():
                intexp = form.save(commit=False)
                intexp.projek = nprojek  # Set projek to the current project
                intexp.save()
                context = {
                    'form': form,
                    'nama_p': nama_p,
                }
                return render(request, 'data_intel/succes.html', context)
        else:
            form = IntExpForm(initial=initial_data)
            context = {
                'form': form,
                'nama_p': nama_p,
                'nprojek': nprojek,
            }
        return render(request, 'data_intel/IntExp.html', context)

    return render(request, 'data_intel/IntExp.html', {'form': form, 'nama_p': request.session.get('nama_proyek', None)})
  
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
    context = None
    form = IntImpForm(None)
    if request.session.get('nama_proyek', None):
        nama_p = request.session.get('nama_proyek', None)
        nprojek = DataProjek.objects.get(nama_proyek=nama_p)
        initial_data = {'projek': nprojek}

        try:
            intimp_instance = IntImp.objects.get(projek=nprojek)
            # If the data already exists, show the "data sudah tersedia" page
            context = {
                'intimp_instance': intimp_instance,
                'nama_p': nama_p,
            }
            return render(request, 'data_intel/DataTersediaImp.html', context)
        except IntImp.DoesNotExist:
            intimp_instance = None

        if request.method == 'POST':
            form = IntImpForm(request.POST, instance=intimp_instance)
            if form.is_valid():
                intimp = form.save(commit=False)
                intimp.projek = nprojek  # Set projek to the current project
                intimp.save()
                context = {
                    'form': form,
                    'nama_p': nama_p,
                }
                return render(request, 'data_intel/succes.html', context)
        else:
            form = IntImpForm(initial=initial_data)
            context = {
                'form': form,
                'nama_p': nama_p,
                'nprojek': nprojek,
            }
        return render(request, 'data_intel/IntImp.html', context)

    return render(request, 'data_intel/IntImp.html', {'form': form, 'nama_p': request.session.get('nama_proyek', None)})


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
    context = None
    form = KendalaForm(None)
    if request.session.get('nama_proyek', None):
        nama_p = request.session.get('nama_proyek', None)
        nprojek = DataProjek.objects.get(nama_proyek=nama_p)
        initial_data = {'projek': nprojek}

        if request.method == 'POST':
            form = KendalaForm(request.POST)
            if form.is_valid():
                kendala = form.save(commit=False)
                kendala.projek = nprojek  # Set projek to the current project
                kendala.save()
                # Remove the session after saving the data
                request.session.pop('nama_proyek', None)
                context = {
                    'form': form,
                    'nama_p': nama_p,
                }
                return render(request, 'data_intel/succes.html', context)
        else:
            form = KendalaForm(initial=initial_data)
            context = {
                'form': form,
                'nama_p': nama_p,
                'nprojek': nprojek,
            }
        return render(request, 'data_intel/Kendala.html', context)

    return render(request, 'data_intel/Kendala.html', {'form': form, 'nama_p': request.session.get('nama_proyek', None)})


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
    context = None
    form = StatusForm(None)
    if request.session.get('nama_proyek', None):
        nama_p = request.session.get('nama_proyek', None)
        nprojek = DataProjek.objects.get(nama_proyek=nama_p)
        initial_data = {'projek': nprojek}

        if request.method == 'POST':
            form = StatusForm(request.POST)
            if form.is_valid():
                status = form.save(commit=False)
                status.projek = nprojek  # Set projek to the current project
                status.save()
                # Remove the session after saving the data
                request.session.pop('nama_proyek', None)
                context = {
                    'form': form,
                    'nama_p': nama_p,
                }
                return render(request, 'data_intel/Status.html', context)
        else:
            form = StatusForm(initial=initial_data)
            context = {
                'form': form,
                'nama_p': nama_p,
                'nprojek': nprojek,
            }
        return render(request, 'data_intel/Status.html', context)

    return render(request, 'data_intel/Status.html', {'form': form, 'nama_p': request.session.get('nama_proyek', None)})



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
    context = None
    form = PerImpForm(None)
    if request.session.get('nama_proyek', None):
        nama_p = request.session.get('nama_proyek', None)
        nprojek = DataProjek.objects.get(nama_proyek=nama_p)
        initial_data = {'projek': nprojek}

        try:
            perimp_instance = PerImp.objects.get(projek=nprojek)
            # If the data already exists, show the "data sudah tersedia" page
            context = {
                'perimp_instance': perimp_instance,
                'nama_p': nama_p,
            }
            return render(request, 'data_intel/DataTersediaPeIm.html', context)
        except PerImp.DoesNotExist:
            perimp_instance = None

        if request.method == 'POST':
            form = PerImpForm(request.POST, instance=perimp_instance)
            if form.is_valid():
                perimp = form.save(commit=False)
                perimp.projek = nprojek  # Set projek to the current project
                perimp.save()
                context = {
                    'form': form,
                    'nama_p': nama_p,
                }
                return render(request, 'data_intel/succes.html', context)
        else:
            form = PerImpForm(initial=initial_data)
            context = {
                'form': form,
                'nama_p': nama_p,
                'nprojek': nprojek,
            }
        return render(request, 'data_intel/PerImp.html', context)

    return render(request, 'data_intel/PerImp.html', {'form': form, 'nama_p': request.session.get('nama_proyek', None)})



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

class StatusListCreate(generics.ListCreateAPIView):
    queryset = Status.objects.all()
    serializer_class = StatusSerializer

def status_form_view(request):
    projek_list = DataProjek.objects.all()
    return render(request, 'data_intel/status_form.html',{'projek_list':projek_list})

class ProjekList(generics.ListAPIView):
    queryset = ProjectInfo.objects.all()
    serializer_class = ProjectInfoSerializers

def project_view(request):
    api_url = 'http://127.0.0.1:8001/api/projects/'  # URL yang benar ke API myapp1
    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        projek_list = data.get('projects', [])  # Ambil data dari key 'projects'
        
        # Simpan data ke dalam model ProjectInfo
        for projek in projek_list:
            # Ambil atau buat DataProjek yang sesuai
            data_projek, created = DataProjek.objects.get_or_create(
                nama_proyek=projek['nama_project']
            )

            ProjectInfo.objects.update_or_create(
                nama_project=projek['nama_project'],
                defaults={
                    'tujuan_project': projek['tujuan_project'],
                    'tangmul_project': projek['tangmul_project'],
                    'tangsel_project': projek['tangsel_project'],
                    'pic_project': projek['pic_project'],
                    'status_project': projek['status_project'],
                    'biaya': projek['biaya'],
                    'projek': data_projek  # Set projek dengan data_projek yang dibuat atau ditemukan
                }
            )
    else:
        projek_list = []

    # Ambil semua data dari ProjectInfo untuk ditampilkan di template
    saved_projects_info = ProjectInfo.objects.all()
    return render(request, 'data_intel/projekinfo.html', {
        'projek_list_info': saved_projects_info
    })