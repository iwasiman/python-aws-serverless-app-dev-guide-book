# 前処理は省略

def lambda_handler(event, context)
    try:
        try:
            # RDBで言うと select * from dynamodb_tbl where status = 'Uploaded'; のフルスキャンを敢行!
            response = table.scan(
                FilterExpression=Attr('status').eq('Uploaded')
            )
        except ClientError as e:
            # エラーログとエラーレスポンス
        else:
           # 変数responseをJSON化、ボディに入れて200の正常応答を返す
    except:
