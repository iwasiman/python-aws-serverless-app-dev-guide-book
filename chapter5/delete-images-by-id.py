def lambda_handler(event, context):
    try:
        # /images/{id}の部分を取得
        photo_id = event['pathParameters']['id']
        try:
            # DynamoDBをキー指定で1アイテム取得
            response = table.get_item(
                Key='photo_id' = photo_id}
            )
            if 'item' not in response:
                # ロギングと404 Not Foundでエラーレスポンス
            else:
                # RDBなら delete from dynamodb_tbl where photo_id = 1234;
                response = table.delete_item(
                    Key={'photo_id' = photo_id}
                )
        except ClientError as e:
            # ロギングと400 Internal Server Errorのエラーレスポンス
        else:
            # 正常終了。ボディは空、204 No Contentで正常レスポンス
    except Exception as e:
        # ロギング
