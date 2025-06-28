from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from artikel.models import Artikel, Kategori
from artikel.forms import ArtikelForm, KategoriForm, UserEditForm
from django.contrib.auth.hashers import make_password
from django.shortcuts import render
import requests

def in_operator(user):
    return user.groups.filter(name='Operator').exists()

def registrasi(request):
    pesan = ""
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        role = request.POST['role']

        if password1 != password2:
            pesan = "Password tidak cocok"
        elif User.objects.filter(username=username).exists():
            pesan = "Username sudah digunakan"
        else:
            user = User(
                username=username,
                first_name=first_name,
                last_name=last_name,
                password=make_password(password1),
            )
            user.save()

            # Tambah ke grup jika diperlukan
            from django.contrib.auth.models import Group
            if role == "admin":
                admin_group, _ = Group.objects.get_or_create(name="Admin")
                user.groups.add(admin_group)
            elif role == "user":
                user_group, _ = Group.objects.get_or_create(name="User")
                user.groups.add(user_group)

            pesan = "Registrasi berhasil. Silakan login."

    return render(request, 'auth/registrasi.html', {"pesan": pesan})


# ========== USER BIASA ==========


@login_required(login_url='/auth-login')
def artikel_detail(request, id_artikel):
    artikel = get_object_or_404(Artikel, id=id_artikel)
    template_name = "dashboard/pengguna/artikel_detail.html"
    return render(request, template_name, {"artikel": artikel})

@login_required(login_url='/auth-login')
def artikel_list(request):
    template_name = "dashboard/pengguna/artikel_list.html"
    artikel = Artikel.objects.filter(created_by=request.user)
    return render(request, template_name, {"artikel": artikel})

@login_required(login_url='/auth-login')
def artikel_tambah(request):
    template_name = "dashboard/pengguna/artikel_forms.html"
    form = ArtikelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, "Berhasil menambahkan artikel")
        return redirect("artikel_list")
    return render(request, template_name, {"form": form})

@login_required(login_url='/auth-login')
def artikel_update(request, id_artikel):
    template_name = "dashboard/pengguna/artikel_forms.html"
    artikel = get_object_or_404(Artikel, id=id_artikel, created_by=request.user)
    form = ArtikelForm(request.POST or None, request.FILES or None, instance=artikel)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, "Berhasil update artikel")
        return redirect("artikel_list")
    return render(request, template_name, {"form": form})

@login_required(login_url='/auth-login')
def artikel_delete(request, id_artikel):
    artikel = get_object_or_404(Artikel, id=id_artikel, created_by=request.user)
    artikel.delete()
    messages.success(request, "Artikel berhasil dihapus")
    return redirect("artikel_list")


# ========== ADMIN / OPERATOR ==========

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_artikel_list(request):
    template_name = "dashboard/admin/artikel_list.html"
    artikel = Artikel.objects.all()
    return render(request, template_name, {"artikel": artikel})

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_artikel_tambah(request):
    template_name = "dashboard/admin/artikel_forms.html"
    form = ArtikelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, "Artikel berhasil ditambahkan")
        return redirect("admin_artikel_list")
    return render(request, template_name, {"form": form})

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_artikel_update(request, id_artikel):
    template_name = "dashboard/admin/artikel_forms.html"
    artikel = get_object_or_404(Artikel, id=id_artikel)
    form = ArtikelForm(request.POST or None, request.FILES or None, instance=artikel)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, "Artikel berhasil diupdate")
        return redirect("admin_artikel_list")
    return render(request, template_name, {"form": form})

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_artikel_delete(request, id_artikel):
    artikel = get_object_or_404(Artikel, id=id_artikel)
    artikel.delete()
    messages.success(request, "Artikel berhasil dihapus")
    return redirect("admin_artikel_list")


# ========== KATEGORI ==========

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_kategori_list(request):
    template_name = "dashboard/admin/kategori_list.html"
    kategori = Kategori.objects.all()
    return render(request, template_name, {"kategori": kategori})

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_kategori_tambah(request):
    template_name = "dashboard/admin/kategori_forms.html"
    form = KategoriForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, "Kategori berhasil ditambahkan")
        return redirect("admin_kategori_list")
    return render(request, template_name, {"form": form})

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_kategori_update(request, id_kategori):
    template_name = "dashboard/admin/kategori_forms.html"
    kategori = get_object_or_404(Kategori, id=id_kategori)
    form = KategoriForm(request.POST or None, instance=kategori)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request, "Kategori berhasil diupdate")
        return redirect("admin_kategori_list")
    return render(request, template_name, {"form": form})

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_kategori_delete(request, id_kategori):
    kategori = get_object_or_404(Kategori, id=id_kategori)
    kategori.delete()
    messages.success(request, "Kategori berhasil dihapus")
    return redirect("admin_kategori_list")


# ========== MANAGEMENT USER ==========

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_management_user_list(request):
    template_name = "dashboard/admin/user_list.html"
    daftar_user = User.objects.all()
    return render(request, template_name, {"daftar_user": daftar_user})

@login_required(login_url='/auth-login')
@user_passes_test(in_operator)
def admin_management_user_edit(request, user_id):
    template_name = 'dashboard/admin/user_edit.html'
    user = get_object_or_404(User, pk=user_id)

    if request.method == 'POST':
        username = request.POST.get("username")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        is_staff = request.POST.get("is_staff")
        groups_checked = request.POST.getlist("groups")

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.is_staff = True if is_staff == "on" else False
        user.groups.set(Group.objects.filter(id__in=groups_checked))
        user.save()

        messages.success(request, f"Berhasil update user {user.username}")
        return redirect('admin_management_user_list')

    all_groups = Group.objects.all()
    group_user = [group.name for group in user.groups.all()]

    context = {
        'user': user,
        'all_groups': all_groups,
        'group_user': group_user,
    }
    return render(request, template_name, context)

def artikel_teknologi(request):
    url = "https://dev.to/api/articles?tag=technology&per_page=5"
    response = requests.get(url)
    data = response.json()
    return render(request, 'teknologi_api.html', {'artikels': data})

def home(request):
    url = "https://dev.to/api/articles?tag=technology&per_page=5"
    response = requests.get(url)
    if response.status_code == 200:
        artikels = response.json()
    else:
        artikels = []

    return render(request, 'index.html', {
        'artikels': artikels,
    })
