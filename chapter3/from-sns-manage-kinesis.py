kinesis = boto3.client('kinesis') # 関数の外で宣言するとパフォーマンス向上
cloudwatch = boto3.client('cloudwatch')

def lambda_handler(event, context):
    message = json.load(event['Records'][0]['Sns']['Message']) #SNSトピック
    alarm_name = message['AlarmName']
    stream_name = message['Trigger']['Dimensions'][0]['value']
    # ここでアラーム名が対象の物かの判定をしないと、全アラームが対象になってしまう
    # Kinesisから取得
    stream_summ = kinesis.describe_stream_summary(StreamName={ストリーム名})
    curr_open_shard_count = stream_summ['StreamDescriptionSumamry']['OpenShardCount']
    # Kinesisを更新
    response = kinesis.update_shard_count(
        StreamName={ストリーム名},
        TargetShardCount={演算した新しいシャード数},
        ScalingType='UNIFORM_SCALING' # ここは固定
    )
    
    # CloudWatchのアラームを更新する例
    response = cloudwatch.put_metric_alarm(
        AlarmName={アラーム名},
        MetricName='incomingRecords',
        Namespace='AWS/Kinesis',
        Period= ..., #ここから先は設定値
    )
