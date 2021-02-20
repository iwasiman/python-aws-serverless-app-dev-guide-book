# 色々省略

def lambda_handler(event, context):
    try:
        # /images/{id}の部分を取得
        photo_id = event['pathParameters']['id']
        try:
            # DynamoDBをキー指定で1アイテム取得
            # select * from dynamodb_tbl where photo_id = 1234
            response = table.get_item(
                Key={'photo_id' = photo_id}
            )
            if 'item' not in response:
                # ロギングと404 Not Foundでエラーレスポンス
        except ClientError as e:
            # ロギングと400 Internal Server Errorのエラーレスポンス
        else:
            # response['item']をJSON化してボディに入れ、200の正常レスポンス
    except Exception as e:
        # ロギング
