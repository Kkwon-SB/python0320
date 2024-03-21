import json
import pandas as pd

def to_json_custom_seq(group): #seq 개수
    data = group.to_dict('records')
    result_data = []

    for datum in data:
        result_data.append(datum.get('seq_no'))

    return json.dumps(list(result_data))

order_df['seq_no'] = order_group_df.apply(to_json_custom_seq).drop(columns=['sale_date', 'store_code', 'pos_no', 'seq_no'])