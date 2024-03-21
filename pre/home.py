import pandas as pd
import numpy as np
import json

order_df = pd.read_csv('test2.csv')

order_df['sku_qnty'] = order_df['sku_qnty'].fillna(0)
order_df['sku_stlmn_amnt'] = order_df['sku_stlmn_amnt'].fillna(0)
order_df['sku_no'] = order_df['sku_no'].fillna('')

order_df = order_df.astype({
        'total_qnty': 'int',
        'total_sell_amnt': 'int',
        'total_dscn_amnt': 'int',
        'total_stlmn_amnt': 'int',
        'sku_stlmn_amnt': 'int',
        'sku_qnty': 'int',
        'sale_date': 'str',
        'trade_time': 'str'
    })

grouped = order_df.groupby(['sale_date', 'store_code', 'pos_no', 'seq_no']).apply(
    lambda x: {
        'sale_date': x['sale_date'].iloc[0],
        'store_code': x['store_code'].iloc[0],
        'pos_no': x['pos_no'].iloc[0],
        'seq_no': x['seq_no'].iloc[0],
        'st_code': x['st_code'].iloc[0],
        'total_qnty': x['total_qnty'].iloc[0],
        'total_sell_amnt': x['total_sell_amnt'].iloc[0],
        'total_dscn_amnt': x['total_dscn_amnt'].sum(),
        'total_stlmn_amnt': x['total_stlmn_amnt'].iloc[0],
        'trade_time': x['trade_time'].iloc[0],
        
        'sku_cntnt': json.dumps([{
            "sku_no": sku['sku_no'],
            "sku_stlmn_amnt": sku['sku_stlmn_amnt'],
            "sku_qnty": sku['sku_qnty']
        } for _, sku in x.iterrows()]),
        
        'cpn_cntnt': json.dumps(list(x['cpn_no'])),
        'order_dtm': x['sale_date'].iloc[0] + x['trade_time'].iloc[0]
    }
)

for key, value in grouped.items():
    print(value)
