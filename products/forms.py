from django import forms
from . models import Product, HashTag

class ProductForm(forms.ModelForm):
    # 사용자 입력을 받을 해시태그 문자열 필드
    hashtags_str = forms.CharField(required=False)
    # 폼 초기화 시, 'user' 인자를 받아서 저장
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'hashtags_str']

    def save(self, commit=True):
        # 새로운 Product 객체 생성
        product = super().save(commit=False)
        # 'user' 인자가 제공되면, 해당 사용자를 Product에 연결
        if self.user:
            product.user = self.user
        # 데이터베이스에 저장
        if commit:
            product.save()
        
        # 해시태그 객체를 생성하거나 이미 존재하는 객체를 가져옴
        hashtags_input = self.cleaned_data.get('hashtags_str', '')
        hashtag_list = [h for h in hashtags_input.replace(',', ' ').split() if h]
        new_hashtags = []
        for ht in hashtag_list:
            ht_obj, created = HashTag.objects.get_or_create(name=ht)
            new_hashtags.append(ht_obj)

        product.hashtags.set(new_hashtags)
        
        if not commit:
            product.save()
            
        return product