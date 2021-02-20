export default {
  data: function() {
    return {
      //image_url_base, uploadFile, images: [] だけ
    }
  },
  created: {
    // listImagesを呼んで一覧表示
  },
  methods: {
    listImages: function() {
      // ライブラリのaxiosを使ってAPI Gatewayの GET /images をコール、
      // 結果の配列をimagesに入れる
    },
    onFileChange: function() {
      // HTMLのinput type="file"要素のonChangeでここに来る。
      // ファイルの中身をdataプロパティ内に格納。
      // この時点ではまだ送信しない。
      this.uploadFile = event.target.files[0]
    },
    uploadImage: function() {
      // HTMLのbutton要素のアップロードボタンを押したらここの処理。
      let data = {size: this.uploadFile.size, type: this.uploadFile.type}
      // まずaxiosを使ってAPI Gatewayの POST /imagesでID登録、
      // →署名付きURLがレスポンスボディで返る
      // 次に署名付きURLに向かって this.uploadFileをPUT。
      // →これで実体がS3に登録。
      // これも成功したらAPI GatewayにPUT /images で
      // ボディのJSONに status:'Uploaded' を入れて更新
    },
  },
}
  