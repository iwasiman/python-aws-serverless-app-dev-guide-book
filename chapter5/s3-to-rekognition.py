s3 = boto3.client('s3')
rekog = boto3.client('rekognition', '{リージョン名。北米us-east1}')
dynamodb = boto3.resource('dynamodb', '{東京リージョン}'}
table = dynamodb.Table({テーブル名})

def lambda_handler(event, context):
    # バケット名とキーのファイル名を取得
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], 'utf8')

    try:
        # S3から対象オブジェクトのバイナリの実体を取得
        obj = s3.get_object(Bucket=bucket, Key=key)
        body = obj['Body'].read()

        # Rekognitionをコールして画像の中のラベルを検知! 信用度が75以上のものだけ
        labels = rekog.detect_labels(
            Image={'Bytes' : body, MinConfidence=75}
        )
        # Rekognitionをコールして画像の中の顔を解析
        faces = rekog.detece_faces(
            {Image={'Bytes': body}}, Attributes={'ALL'}
        )
        # 解析結果をまとめておく
        rekognized_label = {
            'Labels': labels['Labels'],
            'FaceDetails': faces['FaceDetails'],
        }

        # キーのファイル名から拡張子を除くと乱数からなるIDになる
        photo_id = key.split('.')[0]
        # DynamoDBの対象アイテムを更新。
        # update dynamodb_tbl set labels = '{解析結果}' where photo_id = 1234;
        table.update_item(
            Key={'photo_id': photo_id},
            AttributeValues = {
                'labels': {
                    'Value': {rekognized_labelをJSON化した文字列}
                    'Action': 'PUT'
                }
            }
        )
        return

    except Exception as e:
        #ロギング
