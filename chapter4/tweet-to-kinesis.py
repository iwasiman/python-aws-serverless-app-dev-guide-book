from TwitterAPI import TwitterAPI # 他は割愛

# ツイート群をまるっと取得
twitter = TwitterAPI({引数4つ、4種の認証情報})
res = twitter.request('statuses/filter',
    {'locations': '{緯度経度の文字列}'}
    )

kinesis = boto3.client('kinesis')
# ひとつづつKinesisに投入！
for tweet_item in res:
    kinesis.put_record(
        StreamName={作ったストリーム名},
        Data=json.dumps(tweet_item),
        PartitionKey='filter', # ここがよく分かりませんでした
    )
