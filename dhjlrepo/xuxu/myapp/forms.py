from django import forms
from myapp.models import User


class UserForm(forms.ModelForm):
    code = forms.CharField(required=True, max_length=4, min_length=4,
                           error_messages={
                               'required': '验证码不能为空',
                               'min_length': '验证码必须是4位',
                               'max_length': '验证码必须是4位'
                           })
    telephone = forms.CharField(required=True,max_length=11,min_length=11,
                                error_messages={
                                    'required': '电话号码不能为空',
                                    'min_length': '电话号码必须为11位',
                                    'max_length': '电话号码必须是11位'
                                })

    class Meta:
        model = User
        fields = ['username', 'password', 'telephone']
        error_messages = {
            'telephone': {
                'required': '手机号码不能为空'
            },
            'username': {
                'required': '用户名不能为空'
            },
            'password': {
                'required': '密码不能为空'
            }
        }


