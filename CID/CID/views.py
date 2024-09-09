import io
import pandas as pd
import os
import zipfile

from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404, FileResponse, HttpResponse
from django.conf import settings
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.files.storage import FileSystemStorage

from . import forms

@ login_required
def homepage(request):
    user = request.user
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return render(request, 'homepage.html', context)

@ login_required
def rocc_boms(request):
    return render(request, 'BOMS/rocc_boms.html')

@ login_required
def download(request):
    return render(request, 'download.html')

@ login_required
def download_file(request, filename):
    file_path = os.path.join(settings.MEDIA_ROOT, filename)

    if os.path.exists(file_path):
        response = FileResponse(open(file_path, 'rb'), as_attachment=True)

        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response
    else:
        return Http404("File Not Found")
    
@ login_required
def rocc_drawings(request):
    pdf_url = '/media/1912-00001.pdf'
    return render(request, 'drwgs/rocc_drwgs.html', {'pdf_file': pdf_url})

@ login_required 
def report_bug(request):
    if request.method == 'POST':
        form = forms.BugReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bug_report_success')

    else:
        form = forms.BugReportForm()

    return render(request, 'report_bug.html', {'form': form})

@ login_required
def bug_report_success(request):
    return render(request, 'bug_report_success.html')

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('homepage')
    else:
        form = forms.AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def download_zip(request):

    files = [os.path.join(settings.MEDIA_ROOT, file) for file in os.listdir(settings.MEDIA_ROOT)]

    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, 'w') as zip_file:
        for file_path in files:
            zip_file.write(file_path, arcname=file_path.split('\\')[-1])

    zip_buffer.seek(0)

    response = HttpResponse(zip_buffer, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename="files.zip"'

    return response

def list_files(request):

    media_dir = os.path.join(settings.MEDIA_ROOT)

    files = [file for file in os.listdir(media_dir) if file.endswith('.xlsx')]

    if request.method == "POST":
        selected_file = request.POST.get('selected_file')
        if selected_file:
            file_path = os.path.join(settings.MEDIA_ROOT, selected_file)
            try:
                df = pd.read_excel(file_path)
                df.columns = df.iloc[0]
                df = df[1:]
                data = df.values.tolist()
                columns = df.columns.tolist()
                return render(request, 'display_table.html', {'data': data, 'columns': columns, 'files': files, 'selected_file': selected_file})
            except Exception as e:
                return render(request, 'file_list.html', {'files': files, 'error': str(e)})

    return render(request, 'file_list.html', {'files': files})

# def search_view(request):
#     form = SearchForm(request.GET or None)
#     query = request.GET.get('query', '')

#     if query:
#         results = SearchForm.objects.filter(search=query)
#     else:
#         results = SearchForm.object.all()

#     return render(request, 'search_results.html', {
#         'form': form,
#         'results': results
#     })
