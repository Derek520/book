#导入Library类
from django.template import Library
# 创建类对象,变量名固定
register=Library()

@register.filter
def mod(value):
    # 定义求余函数mod，将value对2求余
    return value%2 == 0