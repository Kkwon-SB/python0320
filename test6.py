# import matplotlib as plt
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import rcParams
rcParams["font.family"] = "Malgun Gothic"
rcParams["axes.unicode_minus"] = False

# 샘플 데이터 로드
df = sns.load_dataset('tips')

df.info()
# plt.bar(x=df['total_bill'], y=df['sex'], height=0.7)
# plt.show()
# # plt.scatter(x=df.index, y=df['A'], label='Gorio')
# # plt.legend(loc='lower right')

# df.info()

df2 = df.groupby('total_bill')
# print(df2.get_group(10))

count_Male = df['sex'].value_counts()['Male']
count_Female = df['sex'].value_counts()['Female']
# print(count_Male)
# print(count_Female)

df3 = df.sort_values(by='total_bill', ascending=False)
print(df3)

# plt.bar(x=df['sex'], height=df['total_bill'])
# plt.show()


# grouped = order_df.groupby(['sale_date', 'store_code', 'pos_no', 'seq_no']).apply(
#     lambda x: pd.Series({
#         'sale_date': x['sale_date'].iloc[0],
#         'store_code': x['store_code'].iloc[0],
#         'pos_no': x['pos_no'].iloc[0],
#         'seq_no': x['seq_no'].iloc[0],
#         'st_code': x['st_code'].iloc[0],
#         'total_qnty': x['total_qnty'].iloc[0],
#         'total_sell_amnt': x['total_sell_amnt'].iloc[0],
#         'total_dscn_amnt': x['total_dscn_amnt'].sum(),
#         'total_stlmn_amnt': x['total_stlmn_amnt'].iloc[0],
#         'trade_time': x['trade_time'].iloc[0],
#         'sku_cntnt': json.dumps([{
#             "sku_no": sku['sku_no'],
#             "sku_stlmn_amnt": sku['sku_stlmn_amnt'],
#             "sku_qnty": sku['sku_qnty']
#         } for _, sku in x.iterrows()]),
#         'cpn_cntnt': json.dumps(list(x['cpn_no'])),
#         'order_dtm': x['sale_date'].iloc[0] + x['trade_time'].iloc[0]
#     })
# )