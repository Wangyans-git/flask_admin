from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,IntegerField, \
    FloatField,FileField,BooleanField,PasswordField

import constants


class LoginForm(FlaskForm):
    """登录表单"""
    username = StringField(label='用户名',render_kw={
        'class': 'form-control',
        'placeholder': '请输入用户名',
    })
    password = PasswordField(label='密码',render_kw={
        'class': 'form-control',
        'placeholder': '请输入密码',
    })

    # 调用validate验证器
    def validate_username(self,field):
        # todo 验证
        username = field.data
        return username


class ProductEditForm(FlaskForm):
    """新增商品表单"""

    name = StringField(label='商品标题',render_kw={
        'class':'form-control',
        'placeholder':'请输入商品标题',
    },description='商品标题不超过30字')
    content = TextAreaField(label='商品描述',render_kw={
        'class':'form-control',
        'placeholder':'请输入商品描述',
    })
    desc = StringField(label='商品简述',render_kw={
        'class':'form-control',
        'placeholder':'请输入商品简述',
    })
    types = SelectField(label='商品类型',
                        choices=constants.PRODUCT_TYPES,
                        render_kw={
                            'class':'form-control',
    })
    price = IntegerField(label='商品价格',render_kw={
        'class':'form-control',
        'placeholder':'请输入商品价格',
    })
    origin_price = FloatField(label='商品原价',render_kw={
        'class':'form-control',
        'placeholder':'请输入商品原价',
    })
    img = FileField(label='商品主图')
    channel = StringField(label='渠道',render_kw={
        'class':'form-control',
        'placeholder':'请输入商品渠道',
    })
    buy_link = StringField(label='链接',render_kw={
        'class':'form-control',
        'placeholder':'请输入商品链接',
    })
    status = SelectField(label='商品状态',choices=(
                        constants.PRODUCT_STATUS),
                         render_kw={
                        'class':'form-control',
                        'placeholder':'商品状态',
    })
    sku_count = IntegerField(label='库存',render_kw={
        'class':'form-control',
        'placeholder':'请输入商品库存',
    })
    remain_count = IntegerField(label='剩余库存',render_kw={
        'class':'form-control',
        'placeholder':'请输入商品剩余库存',
    })
    view_count = IntegerField(label='浏览次数',render_kw={
        'class':'form-control',
        'placeholder':'请输入浏览次数',
    })
    score = IntegerField(label='评分',render_kw={
        'class':'form-control',
        'placeholder':'请输入评分',
    })

    is_valid = BooleanField(label='逻辑删除')
    reorder = IntegerField(label='排序',render_kw={
        'class':'form-control',
        'placeholder':'请输入排序',
    })

