# subview

clip studio paint のサブビューに指定フォルダ内の画像ファイルを一括して登録します  
CLIP STUDIO PAINT が起動している状態で実行しても反映されません  

オプション関係  
EXTENSIONS 画像ファイルは拡張子を指定します jpg / jpeg / png にしてあります  

GUI 仕様
exit 何もせず終了
append フォルダ選択（複数回可）
commit で登録

現在mac / win でとりあえず動くことを確認  
実行形式は win7にて確認　
使用は自己責任にて

考えてること
* psvファイル中のsubviewimagecategoryの内容を別のdbファイルにバックアップし、再利用できるようにする
* 登録できるファイル数の上限の設定と確認（現実的には100枚も同時には、ユーザビリティ上扱いたくないとは思いますが）
