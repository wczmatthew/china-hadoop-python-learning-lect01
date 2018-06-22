'''
    作者：wcz
    版本：v2.0
    日期：01/08/2018
    新增功能：根据输入判断是人民币还是美元 进行相关的转换计算
    知识点： 字符串的末三位截取  s[-3:]
'''

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币的输入
currency_str_value = input('请输入带单位的货币金额:')

# 获取货币单位
unit = currency_str_value[-3:]

print(unit)
# # 将字符串转换为数字
# rmb_value = eval(rmb_str_value)
#
# # 汇率计算
# usd_value = rmb_value / USD_VS_RMB
#
# # 输出结果
# print('美元(USD)金额是:', usd_value)
