from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ProductForm
from .models import Product


def product_list_view(request):
    """모든 제품 목록을 표시합니다."""
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/product_list.html', context)


@login_required
def product_create_view(request):
    """새로운 제품을 생성합니다."""
    if request.method == 'POST':
        form = ProductForm(
            data=request.POST,
            files=request.FILES,
            user=request.user
        )
        
        if form.is_valid():
            form.save()
            messages.success(request, '제품이 성공적으로 등록되었습니다.')
            return redirect('products:product_list')
    else:
        form = ProductForm()

    context = {
        'form': form
    }
    return render(request, 'products/product_form.html', context)


@login_required
def product_detail_view(request, pk):
    """제품의 상세 정보를 표시합니다."""
    product = get_object_or_404(Product, pk=pk)
    product.views += 1
    product.save()
    
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def product_update_view(request, pk):
    """제품 정보를 수정합니다."""
    product = get_object_or_404(Product, pk=pk)
    
    # 작성자 확인
    if product.user != request.user:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('products:product_detail', pk=pk)
    
    if request.method == 'POST':
        form = ProductForm(
            data=request.POST,
            files=request.FILES,
            instance=product
        )
        if form.is_valid():
            form.save()
            messages.success(request, '제품이 성공적으로 수정되었습니다.')
            return redirect('products:product_detail', pk=pk)
    else:
        # 해시태그 초기값 설정
        initial_hashtags = ' '.join(ht.name for ht in product.hashtags.all())
        form = ProductForm(
            instance=product,
            initial={'hashtags_str': initial_hashtags}
        )

    context = {
        'form': form,
        'product': product
    }
    return render(request, 'products/product_form.html', context)


@login_required
def product_delete_view(request, pk):
    """제품을 삭제합니다."""
    product = get_object_or_404(Product, pk=pk)
    
    # 작성자 확인
    if product.user != request.user:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('products:product_detail', pk=pk)
    
    if request.method == 'POST':
        product.delete()
        messages.success(request, '제품이 성공적으로 삭제되었습니다.')
        return redirect('products:product_list')
    
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context)


@login_required
def product_like_view(request, pk):
    """제품 좋아요를 토글합니다."""
    product = get_object_or_404(Product, pk=pk)
    
    if request.user in product.likes.all():
        product.likes.remove(request.user)
        message = '좋아요가 취소되었습니다.'
    else:
        product.likes.add(request.user)
        message = '좋아요가 추가되었습니다.'
    
    messages.success(request, message)
    return redirect('products:product_detail', pk=pk)