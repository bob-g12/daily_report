# daily_report
## アプリ内容
>主に運送会社に向けた勤務管理システム
>
>走行記録や運転手などの記録を投稿できるアプリ
>
>学習を兼ねているため、コメントを多めに残してあります。
>
>下記にて機能の解説をイメージ画像とともに
>記載しています。
## 作成のきっかけ
>所属していた運送会社で、車両記録を紙へ記入しており、
>
>前日の終メーターや車両情報など、記録があればいらない記入を含め
>
>繰り返し作業を毎日行っていたため、効率化したいと思い開発しました。
>
>実用にはまだ機能が足りていないので、使える機能が揃い次第
>
>サイトの公開を検討します。
## サイトの公開
>現在サイトの公開はしておりません
## 使用言語等
### 言語
Python / HTML / CSS / Javascript
### データベース
sqlite3
### 開発ツール
vscode
### 拡張機能
|/|機能|用途|
| ---- | ---- | ---- |
|**`必須`** | Python |VScodeでPythonを使用するため|
|**`必須`** | SQLite |VScodeでSQLiteを使用するため|
|**`必須`** | Bootstrap 5 Quick Snippets |VScodeでBootstrapを使用するため|
|**`必須`** | Django Template |クォーテーションの入れ子を解消するために実装|
|| Japanese Language Pack for Visual Studio Code|vscodeを日本語表記に変更するため|
|| Git Lens|コミット時期を表示するため|
|| Git History|コミット履歴の確認等をするため|
|| jQuery Code Snippets|jQueryメソッドの記述を補完|
|| Pylance|Pythonの入力補完|

## 機能
### toppage
>画面右上の投稿ボタンにて投稿ページへ進みます。
>
>投稿の左、topでtoppageへ戻れます。
>
>各投稿の車両番号/お名前/乗車日が表示。

<img width="500" alt="image" src="https://github.com/bob-g12/daily_report/assets/126374166/7fef6584-3c2e-4b23-bbab-a069763a5104">

### 投稿画面
>投稿は一部カレンダーや選択肢による入力が可能です。必須マークのある項目が抜けていると投稿出来ず、入力を求めます。

<img width="500" alt="image" src="https://github.com/bob-g12/daily_report/assets/126374166/0b7c94ce-9db3-491d-92c6-f936bde8f009">
<img width="500" alt="image" src="https://github.com/bob-g12/daily_report/assets/126374166/aa203f28-89dc-41bb-b021-b0d60560de00">

### 編集/削除
>投稿ごとに編集ボタンがあり、過去の投稿内容が反映された状態から編集ができます。
>
>投稿ごとに削除ボタンがあり、押すとダイアログにて確認を挟み、投稿の削除ができます。

<img width="500" alt="image" src="https://github.com/bob-g12/daily_report/assets/126374166/f54a1beb-bf22-4f7b-b045-d605d42c27c6">
<img width="500" alt="image" src="https://github.com/bob-g12/daily_report/assets/126374166/1ca40ba6-d2ff-419b-9ef9-f564a349a109">

### update予定
>ログイン機能を実装し、削除権限を持ったアカウントや、扱う投稿の制限などを可能にする。
>
>投稿データをExcelに挿入する機能
>
>ダイアログのデザインを変更
>
>車両ごとに投稿ページをわける
>
>車両の点検項目を追加
>
>車両の前日記録を参照








