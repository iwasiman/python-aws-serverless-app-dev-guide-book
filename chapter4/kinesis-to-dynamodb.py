
# 変数tableに対象のDynamoDBテーブルをいれておく

def lambda_handler(event, context):
    try:
        batch_item_list = []
        for records in event['Records']:
            # Kinesis から取り出すときにデコードがいる
            payload = base64.b64decode(record['kinesis']['data'])
            data = json.loads(payload)
            item = {dataを元に1アイテム分を準備}
            batch_item_list.append[item]

        # 最大25件も意識せずにバッチ処理可能
        with table.batch_writer() as batch: 
            for item in batch_item_list:
                batch.put_item(Item=item)
            return

    except Exception as e:
        # エラー処理
        raise

