from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignupForm, ProfileForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import User
from products.models import Product

# 회원가입 기능
def signup_view(request):
    # 회원가입 처리 및 자동 로그인
    if request.method == "POST":
        form = SignupForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:signup')
    # 회원가입 페이지 렌더링
    else:
        form = SignupForm()
    
    return render(request, 'accounts/signup.html', {'form':form})

# 로그인 기능
def login_view(request):
    # 이미 로그인 되어 있으면 메인페이지로 이동
    if request.user.is_authenticated:
        return redirect("products:product_list")
    
    # 로그인 처리
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("products:product_list")
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})

# 로그아웃 기능
@login_required
def logout_view(request):
    logout(request)
    return redirect('accounts:login')

# 프로필 기능
@login_required
def profile_view(request, username):
    # 프로필 조회
    profile_user = get_object_or_404(User, username=username)
    # 등록 물품
    my_products = Product.objects.filter(user=profile_user)
    # 찜한물품
    liked_prducts = profile_user.liked_products.all()
    # 팔로잉 여부
    is_following = request.user.follows.filter(pk=profile_user.pk).exists()

    context = {
        'profile_user': profile_user,
        'my_products': my_products,
        'liked_products' : liked_prducts,
        'is_following' : is_following,
    }
    return render(request, 'accounts/profile.html', context)

# 프로필 수정 기능
def profile_edit(request, username):
    # 프로필 수정 권한 확인
    if request.user.username != username:
        return redirect('accounts:profile', username=username)
    # 프로필 조회
    user = get_object_or_404(User, username=username)
    # 프로필 수정 처리
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile', username=username)
    # 프로필 수정 페이지 렌더링
    else:
        form = ProfileForm(instance=user)
    return render(request, 'accounts/profile_edit.html', {'form':form})                    

# 팔로우 기능
def follow_view(request, username): 
    # 팔로우 대상 조회
    target_user = get_object_or_404(User, username=username)
    # 팔로우 대상이 로그인한 사용자가 아니면
    if target_user != request.user:
        # 팔로우 대상이 로그인한 사용자가 팔로우 하고 있으면 팔로우 취소
        if request.user.follows.filter(pk=target_user.pk).exists():
            request.user.follows.remove(target_user)
        # 팔로우 대상이 로그인한 사용자가 팔로우 하고 있지 않으면 팔로우
        else:
            request.user.follows.add(target_user)
    return redirect('accounts:profile', username=username)