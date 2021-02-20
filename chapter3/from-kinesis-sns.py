

kinesis = boto3.client('kinesis')
kinesis.put_record(
    StreamName={ストリーム名},
    Data={入れる内容},
    PartitionKey={グループ分けに使われるパーティションキー。サンプルでは現在時刻より}
    )