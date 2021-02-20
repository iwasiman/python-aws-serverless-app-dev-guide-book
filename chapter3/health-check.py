SITE = os.environ['site'] # コードの外側、環境変数から取得できる
EXPECTED = os.environ['expected'] # ここにチェック対象の文字列を入れておく

def validate(res):
    return EXPECTED in str(res)

def lambda_handler(event, context):
    try:
        if not validate(urlopen(SITE).read()):
            raise Exception('https://awas.amazon.com/ にAWSの文字がない!')
    except:
        print('サイトが死んでる!')
        raise
    else:
        print('サイトは生きてるよ')
        return event['time']
    finally:
        print('定期チェック終了')
