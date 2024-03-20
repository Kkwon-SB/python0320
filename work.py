
import json
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

result_columns = [
    'sale_date',
    'store_code',
    'pos_no',
    'seq_no',
    # 'st_code',
    'total_qnty',
    'total_sell_amnt',
    'total_dscn_amnt',
    'total_stlmn_amnt',
    'sku_cntnt',
    'cpn_cntnt',
    'order_dtm'
]

order_df = pd.read_csv('test.csv')


result_df2 = order_df.sort_values(by=['sale_date','store_code','pos_no','seq_no'], ascending=False)

cnt = 0

for index, data in result_df2.iterrows():
    # print(f"{data['sale_date']}|{data['store_code']}|{data['pos_no']}|{data['seq_no']}") 
    print(index, data)

    cnt += 1
    if cnt > 20:
        break


order_df = order_df.drop(['st_code'], axis=1)

order_df['sku_qnty'] = order_df['sku_qnty'].fillna(0) 
order_df['sku_stlmn_amnt'] = order_df['sku_stlmn_amnt'].fillna(0)
order_df['sku_no'] = order_df['sku_no'].fillna('') 
order_df = order_df.astype({ 
        'total_qnty': 'int',
        'total_sell_amnt': 'int',
        'total_dscn_amnt': 'int',
        'total_stlmn_amnt': 'int',
        'sku_stlmn_amnt': 'int',
        'sku_qnty': 'int'
    })


cnt = 0


order_group_df = order_df.groupby(['sale_date', 'store_code', 'pos_no', 'seq_no'], as_index=False) 


def to_json_custom_total(group): 
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_datum = {
            'total_qnty': datum.get('total_qnty'),
            'total_sell_amnt': datum.get('total_sell_amnt'),
            'total_dscn_amnt': datum.get('total_dscn_amnt'),
            'total_stlmn_amnt': datum.get('total_stlmn_amnt')
        }
        result_data.append(result_datum)

    return json.dumps(list(result_data))

def to_json_custom_sku(group): #sku 개수
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_datum = {
            'sku_no': datum.get('sku_no'),
            'sku_stlmn_amnt': datum.get('sku_stlmn_amnt'),
            'sku_qnty': datum.get('sku_qnty')
        }
        result_data.append(result_datum)

    return json.dumps(list(result_data))

def to_json_custom_cpn(group): #쿠폰 개수
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('cpn_no'))

    return json.dumps(list(result_data))

def to_json_custom_total_qnty(group): #쿠폰
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('total_sell_amnt'))

    return json.dumps(list(result_data))

def to_json_custom_total_sell_amnt(group): #쿠폰
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('total_dscn_amnt'))

    return json.dumps(list(result_data))

def to_json_custom_total_dscn_amnt(group): #쿠폰
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('total_stlmn_amnt'))

    return json.dumps(list(result_data))

def to_json_custom_total_stlmn_amnt(group): #쿠폰
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('total_qnty'))

    return json.dumps(list(result_data))

def to_json_custom_store(group): #가게 개수
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('store_code'))

    return json.dumps(list(result_data))

def to_json_custom_pos(group): #pos 개수
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('pos_no'))

    return json.dumps(list(result_data))

def to_json_custom_seq(group): #seq 개수
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('seq_no'))

    return json.dumps(list(result_data))

def to_json_custom_seq(group): #seq 개수
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('seq_no'))

    return json.dumps(list(result_data))



order_df['sku_cntnt'] = order_group_df.apply(to_json_custom_sku).drop(columns=['sale_date', 'store_code', 'pos_no', 'seq_no'])
order_df['cpn_cntnt'] = order_group_df.apply(to_json_custom_cpn).drop(columns=['sale_date', 'store_code', 'pos_no', 'seq_no'])
order_df['order_dtm'] = order_df['sale_date'] + order_df['trade_time']

result_df = order_df[result_columns]

result_df2 = result_df.sort_values(by=['sale_date','store_code','pos_no','seq_no'], ascending=False)


# result_df2.info()

# cnt = 0

# for index, data in result_df2.iterrows():
#     print(f"{data['sale_date']}|{data['store_code']}|{data['pos_no']}|{data['seq_no']}|{data['sku_cntnt']}") 

#     cnt += 1
#     if cnt > 20:
#         break