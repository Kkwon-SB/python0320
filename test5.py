import pandas as pd

# 예제 데이터 생성
data = {
    'sale_date': ['2024-03-20', '2024-03-20', '2024-03-20', '2024-03-21', '2024-03-21','2024-03-22', '2024-03-22',],
    'total_price': [50000, 30000, 75000, 25000, 60000, 1500, 34700]
}

sales_df = pd.DataFrame(data)

result2 = sales_df.groupby(['sale_date']).apply(
    lambda x: pd.Series({
        'total_price': x['total_price'].sum(),
        'total_price2': x['total_price'].sum()
        
    })
)

# result2.info()

# print(result2)
import matplotlib.pyplot as plt

# print(sales_df.groupby('sale_date').mean())

def get_top5(x):
    # 나이를 기준으로 정렬하여 상위 5개 행을 반환
    return x.sort_values('sale_date').head()

result = sales_df.groupby('sale_date').apply(get_top5)

# result.info()
# print("\n\n",result)

result2 = sales_df.groupby('sale_date')



result3 = sales_df.groupby('sale_date').apply(lambda x: x+1000)


# # 각 그룹에 대한 정보 확인
# for date, group_data in result3.iteritems():
#     print(f"Date: {date}")
#     print(group_data)

# 각 그룹에 대한 정보 확인
for a, b in result2:
    print(f"Date: {a}")
    print(f"total_price: {b}")

