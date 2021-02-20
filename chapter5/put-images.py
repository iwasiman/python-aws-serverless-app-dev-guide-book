# 最初にJSONの中にFloat型があってもうまく処理してくれるクラスを用意

# ボディに3つのキーが入っていればバリデーションOK
def validate(body):
    return body.keys() >= {'photo_id', 'timestamp', 'status'}

def lambda_handler(event, context):
    # またVue.jsの中のaxiosから飛んでくるのでボディを取得
    body = json.load(event['body']) 
    if not validate(body):
        # エラーレスポンスを返して終了

    photo_id = body['photo_id']
    timestamp = body['timestamp']
    status = body['status'] # 'Uploaded'が渡っててくる
    try:
        try:
            # DynamoDBのテーブル、idで指定したアイテムのstatusだけを、
            # 画面から渡ってくる値に更新
            # 抜けてるけどtimestampも一緒に更新する意図?
            # update dynamodb_tbl set status = 'xx', timestamp = yy where photo_id = 1234;
            table.update_item(
                Key={'photo_id': photo_id},
                AttributeUpdates={
                    'status': {'Value': status, 'Action': 'PUT'}
                }
            )
            response = table.get_item(
                Key={'photo_id': photo_id}
            )
        except ClientError as e:
            # ロギングとエラーレスポンス
        else:
            # response['item']の内容をボディにJSON形式で入れ、200の正常レスポンスを返す
    except Exception as e:
        # エラーをロギング
