import appConfig from './config'; // UserPoolId、UserPoolClientIdがここから取れる
import * as AWS from "aws-sdk";
import {
  CognitoUserPool, CognitoUserAttribute, CognitoUser
} from "amazon-cognito-identity-js";

export default {
  signup: function(username, email, password) {
    // サインアップ画面からユーザ名、メアド、パスワードをもってこの関数へ。
    // 固定のUserPoolId、UserPoolClientIdを使ってCognitoUserPoolクラスを
    // 作り、メアドも入力情報に含めてCognito側のsingup()をコール。
  },

  confirm: function(username, confirmation_number) {
    // 確認画面でユーザ名、メールに書いてある確認番号を入れたらこの関数へ。
    // 固定のUserPoolId、UserPoolClientIdを使ってCognitoUserPoolクラスを作り、
    // ユーザ名も入れたCognitoUserクラスを作り、
    // 確認番号を入力にしてCognito側のconfirmRegjstration() をコール。
    // どれもreturn new Promise(() => ...の中にラップすることで非同期処理を
    // 閉じ込め、Vueコンポーネント側から呼びやすくする。
  },

  authenticate: function(email, password) {
    // サインイン画面でメアドとパスワードを入れたらこの関数へ。
    // 固定のUserPoolId、UserPoolClientIdを使ってCognitoUserPoolクラスを作り、
    // ユーザ名も入れたCognitoUserクラスを作り、
    // メアドとパスワードを入力にCognito側の authenticateUsser() をコール。
    // コールバックが成功/失敗の他に強制パスワード変更もある。
  },

  loggedIn: function() {
    // Vueコンポーネントで実装された各画面の初期表示時にこの関数へ。
    // 固定のUserPoolId、UserPoolClientIdを使ってCognitoUserPoolクラスを作り、
    // getCurrentUser() を呼ぶと今のユーザーが取得できる。
    // セッションが取得出来てメアドを持ってればログインOKとしtrueを返す。
  },

  logout: function() {
    // ログアウトボタンからこの関数へ。
    // 固定のUserPoolId、UserPoolClientIdを使ってCognitoUserPoolクラスを作り、
    // cognitoUserPool.getCurrentUser().signOut() とするとログアウト処理。
  },

  get_id_token: function() {
    // 固定のUserPoolId、UserPoolClientIdを使ってCognitoUserPoolクラスを
    // 作り、cognitoUserPool.GetCurrentUser().getSession() 。
    // その結果からgetIdToken().getJwtToken() するとトークンの文字列が取得できる。
  },
}
