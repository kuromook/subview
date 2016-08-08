# subview

clip studio paint のサブビューに指定フォルダ内の画像ファイルを一括して登録します  
CLIP STUDIO PAINT が起動している状態で実行しても反映されません  

オプション関係  
ASK_DIR をTrueにした場合、ソースフォルダを選択するフォルダ選択ダイアログが立ち上がります。  
ASK_DIR をFalseにした場合、自動的に~/Desktop/tmpフォルダを対象にします  
EXTENSIONS 画像ファイルは拡張子を指定します jpg / jpeg / png にしてあります  
REPLACE をTrueにする場合、subview の画像を入れかえます（Falseの場合、おきかえます）


現在mac / win でとりあえず動くことを確認  
実行形式は win7にて確認　
使用は自己責任にて

考えてること
* psvファイル中のsubviewimagecategoryの内容を別のdbファイルにバックアップし、再利用できるようにする
* 登録できるファイル数の上限の設定と確認（現実的には100枚も同時には、ユーザビリティ上扱いたくないとは思いますが）
