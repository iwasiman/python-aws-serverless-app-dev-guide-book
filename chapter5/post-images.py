# ハンドラの外側でパフォーマンス向上
dynamodb = boto3.resouces('dynamodb')
table = dynamodb = dynamodb.Table({テーブル名})


# UUIDからランダムなIDを生成
def generate_id():
    return str(uuid.uuid4())

# DynamoDBは数値のfloat型を使えないので、現在日付はintに変換
def get_timestamp():
    now = datetime.datetime.utcnow()
    return int(now.timestamp())

# 1時間使える署名付きURL コード例だと引数3にcontent-typeがあるが、
# その後の説明だと抜けてるような?
def get_presigned_url(bucket_name, key):
    s3 = boto3.client('s3')
    url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={'Bucket': bucket_name, 'Key': key},
        Expiresln = 60*60,
        HttpMethod='PUT'
    )
    return url

def lambda_handler(event, context):
    # 画面側のVue.jsの中からaxiosを使って送信してくる
    body = json.load(event['body'])
    url = get_presigned_url({バケット名}, generate_id())
    item = {IDやタイムスタンプなど1アイテム分を準備。staus:'Waiting'}
    try:
        # insert into dynamodb_tbl values(itemの各属性); 的な処理
        table.put_item(Item=item)
    except ClientError as e:
        # ログしてエラーレスポンス
    else:
        # ボディに生成した署名付きURLのurlをJSON形式で入れて、200の正常レスポンスを返す
