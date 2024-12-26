from django import forms
from . models import Product, HashTag

class ProductForm(forms.ModelForm):
    hashtags_str = forms.CharField(required=False)

    # 상품폼을 생성할떄 중요한건 사용자다 왜냐! 이상품을 사용자가 등록해서
    # 그러므로 사용자를 뽑아서 해당 상품이랑 연결시켜 줘야한다

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None) #user인자를 뽑는것
        super().__init__(*args, **kwargs) #부모 클래스 초기화
    
    class Meta:
        model = Product
        fields = ['title', 'description', 'image', 'hashtags_str']
    


# save 메서드는 폼에서 입력한 데이터를 db에 적재하는 놈이다!
    def save(self, commit=True):
        # 부모 클래스의 save 매서드를 호출하되, commit=False 할 것이다 -> 해당 상품을 들고도오되 db에는 product 저장하지 않겠다.
        # 1. product 객체를 생성하고, 추가 작업(해시태그 처리)을 완료한뒤에서 commit을 한다(db에 반영한다.)
        # 2. user와 연결을 또 시켜줘야합니다. 그 결과를 db에 적재하기 위해서 일단 commit을 false로 둔다.
        product = super().save(commit=False)
        
        if self.user:
            product.user = self.user
        
        if commit:
            product.save()
        
        # 해시태그 처리
        # 입력받은 hashtag_str 문자열을 쉼표나 공백으로 구분해볼게요! (제한)
        # 각 해시태그를 db에 저장하거나, 이미 존재하면 가져올거임
        hashtags_input = self.cleaned_data.get('hashtags_str', '')
        hashtag_list = [h for h in hashtags_input.replace(',', ' ').split() if h]
        new_hashtags = []
        for ht in hashtag_list:
            ht_obj, created = HashTag.objects.get_or_create(name=ht)
            new_hashtags.append(ht_obj)
        
        # 다대다 관계 설정
        product.hashtags.set(new_hashtags)
        
        if not commit:
            product.save()
            
        return product