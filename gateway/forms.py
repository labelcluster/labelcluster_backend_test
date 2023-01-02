from django import forms

from .models import Gateway

# 写文章的表单类
class GatewayForm(forms.ModelForm):
    class Meta:
        # 定义表单包含的字段
        model = Gateway
        fields = ('app_id',
    'type',
    'timestamp',
    'sign',
    'sign_type',
    'encrypt_type',
    'biz_data')