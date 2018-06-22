'''
    作者：wcz
    版本：v4.0
    日期：22/06/2018
    v2.0：根据输入判断是人民币还是美元 进行相关的转换计算
    v3.0：程序可以一直运行，直到用户选择退出
    V4.0：将汇率兑换封装到函数中

    知识点： 字符串的末三位截取  s[-3:]
            字符串除了末3位    s[:-3]
'''

def convert_currency(im, er):
    '''
        汇率兑换
    '''
    out = im * er
    return out


# 汇率
USD_VS_RMB = 6.77

# 带单位的货币的输入
currency_str_value = input('请输入带单位的货币金额(退出程序请输入Q):')

# 获取货币单位
unit = currency_str_value[-3:]

if unit == 'CNY':
    exchange_rate = 1 / USD_VS_RMB
elif unit == 'USD':
    exchange_rate = USD_VS_RMB
else:
    # 其他情况
    exchange_rate = -1

if exchange_rate != -1:
    in_money = eval(currency_str_value[:-3])
    out_money = convert_currency(in_money, exchange_rate)
    print('兑换后的金额：', out_money)
else:
    print('不支持该种货币')


# # 将字符串转换为数字
# rmb_value = eval(rmb_str_value)
#
# # 汇率计算
# usd_value = rmb_value / USD_VS_RMB
#
# # 输出结果
# print('美元(USD)金额是:', usd_value)
