# 映画の台詞と歌詞で学ぶヒンディー語

映画の台詞と歌詞を題材に、ヒンディー語の表現がどのように意味を作るかを学ぶノート集です。デーヴァナーガリー文字の**原文・日本語訳・文法解説**を結び付け、日本語で説明します。

## 保存先のルール

「映画追加」「フォルダ作成」「資料保存」は、**GitHub リポジトリ `alipasa727/hindi_movie` 内**への作成・保存を意味します。クラウド環境の作業先は `/workspace/hindi_movie` です。外部ストレージには、サービス名と保存先を明示した依頼がある場合だけ保存します。

保存先・アクセス範囲・最新状態の確認・GitHub への反映は [AGENTS.md](AGENTS.md) を参照してください。

## 学習の方針

原文を読み、語と語の関係や活用を追い、訳の理由が分かることを目指します。会話では口語の省略・敬意・人物関係を、歌詞では比喩・反復・詩的な語順を扱います。本文はデーヴァナーガリー文字を基本にし、ローマ字・カタカナは必要な場合の補助にします。

語義・基本形・文法の説明は、AIが持つヒンディー語の知識を基本にします。外部の辞書・文法書の検索や照合記録は必須にしません。一般的な説明、本文への当てはめ、場面からの推定を分け、不確かな点はその箇所で示します。実際に参照していない資料を出典として挙げません。

## 教材の基本構成

台詞は意味が続く発言・やり取り、歌詞は節・サビなどのまとまりごとに、次の5項目を置きます。

1. **本文**：出典で確認したヒンディー語原文だけを掲載します。
2. **直訳**：主語・目的語・修飾関係や活用の働きを追える日本語訳にします。
3. **語彙説明**：本文の形と基本形を対応させ、本文での意味・変化を説明します。
4. **文法説明**：「誰が・何をするか」の骨格から文の仕組みを説明します。
5. **補足**：背景、比喩、訳で補った内容、表記差、不確かな点を扱います。

語彙は次の表にまとめます。

| 本文の形 | 基本形 | 品詞 | 意味 | 活用・語尾の働き |
| --- | --- | --- | --- | --- |
| 本文中の語 | 基本形 | `N.M.SG`・`V.FUT.1SG.F` など | この文での語義 | 本文の形への変化と文中での働き |

文法用語には日本語の説明を添え、実際の本文に必要な事項を扱います。

性・数・人称は、語彙表の **品詞欄** に `N.M.SG`・`ADJ.F.SG`・`V.FUT.1SG.F`・`AUX.PRS.3SG` のように記載します。複数語は語ごとに示します。略語は文法凡例に統一し、一致先や活用の理由は「活用・語尾の働き」と文法説明で扱います。

代名詞にも `PRON.1SG.M/F` のように性・数を付けます。`M/F` は性による語形の区別がない共通形です。所有形は `PRON.F.PL`（所有形・所有者1SG）のように、名詞への一致と所有者の情報を分けます。

略語とグロスの表記は [ヒンディー語の文法凡例とグロス](GRAMMAR_LEGEND.md) にまとめています。性・数・人称・格・相などの略語一覧と、語別の分析例を参照できます。

| 項目 | 説明する内容 |
| --- | --- |
| 後置詞・斜格 | 名詞や代名詞の後ろで「〜に・〜から」などの関係を示す語と、その前での語形変化 |
| 性・数・一致 | 名詞の性と数、形容詞・動詞が何に合わせて形を変えるか |
| 時制・相・助動詞 | いつのことか、習慣・進行・完了など、動作の捉え方と助動詞の働き |
| ने・को と一致 | 完了相の他動詞文などでの主語・目的語の示し方と、動詞が一致する相手 |
| 複合動詞・接続形 | 動詞の組み合わせや、動作をつなぐ形の意味 |
| 敬意・否定・疑問・命令・条件 | 相手との関係や発言の意図が形にどう現れるか |
| 修飾・関係詞・相関詞 | 名詞を説明するまとまりや、節どうしの対応 |
| 口語・詩的表現 | 省略・語順・比喩・反復と、通常の表現との違い |

教材の冒頭に作成手順などの前置きを置きません。歌詞の先頭見出しは曲名だけにします。意味の理解に必要な注記だけを該当箇所に置きます。補足がなければ空欄にし、復習問題・練習・学習進捗の記録は追加しません。

## 原文の確認

**台詞・歌詞・学習用の例文は自作しません。** 記憶や生成文を作品の原文として掲載しません。ユーザー提供本文・画像、本編・公式字幕・公式歌詞、台詞集・映画記事・歌詞サイトなど、実際に読んだ資料から原文を採用します。

ヒンディー語の原語版と吹替版を区別し、音声・字幕・掲載本文それぞれの言語を確認します。他言語版の原文や分析をそのままヒンディー語の確認結果にしません。検索結果の断片や自動翻訳だけで原文を確定しません。

引用は学習に必要な短い範囲にし、省略・反復を明らかにします。異なる資料や離れた場面を合成しません。日本語訳で補った内容や場面に応じた言い換えは、補足で説明します。

出典欄・確認記録、`source`・`sources` フォルダ、添付資料のコピーは、明示的な依頼がなければ追加しません。原文を読むことと本編の音声・字幕を照合することは区別し、未確認の内容は断定しません。確認方針は [SOURCES.md](SOURCES.md) を参照してください。

## ノートの整理

映画ごとに次の構成にします。`movie.md` は作成しません。

```text
movies/<映画名>-<公開年>/
├── dialogues/
│   └── dialogue.md
└── songs/
    └── Song-Title.md
```

台詞は作品ごとに1ファイルへ追記し、既存の番号と `dialogue-001` 形式のアンカーを保ちます。作品名はフォルダ名で示し、台詞ファイルとひな形には作品タイトルや「台詞集」の見出しを置きません。冒頭に各節へのリンク付き目次を置き、台詞の追加時には目次も更新します。歌詞は曲ごとに1ファイルにし、英字の曲名の空白はハイフンにします。同じ曲の追加は同じファイルにまとめます。各ノートに作品一覧への戻りリンクは付けません。

新規作成には [台詞ひな形](movies/_template/dialogues/dialogue.md)・[歌詞ひな形](movies/_template/songs/Song-Title.md) を使います。

個別指定による例外として、Sholay の「कितने आदमी थे?」から始まる今回の抜粋だけは、`dialogues/Kitne-Aadmi-The.md` に独立して保存します。この例外は他の台詞には適用しません。

## 保存先・書式の検査

教材の変更後、コミット前に `python3 scripts/check_notes.py` を実行します。保存パス、各節の5区分、語彙表の列、台詞の番号とアンカーを検査します。対象パスを引数で指定すると、リポジトリ外への保存先もエラーになります。

GitHub Actions でも同じ検査を実行します。この検査は翻訳の正確さや指示を読んだことを判定せず、リポジトリ外のファイルは自動検出しません。Actions の失敗を理由にマージを禁止するには、別途ブランチ保護の設定が必要です。

### クラウド環境の開始位置への案内

クラウド環境で `python3 /workspace/hindi_movie/scripts/setup_workspace.py` を実行すると、`/workspace/AGENTS.md` にプロジェクトの指示への案内を配置します。既存の異なる指示は上書きしません。案内の原本と配置処理はこのリポジトリで管理します。

案内には、保存先が確定済みであることと、保存先の質問・確認フォーム・外部ストレージの探索より先にこのリポジトリの指示を読むことを明記しています。環境起動待ちや接続障害は、保存先を再質問する理由にしません。

配置後は `python3 /workspace/hindi_movie/scripts/setup_workspace.py --check` で未配置・原本との不一致を検出します。検査は既存の案内を変更しません。起動処理では、配置コマンドに続けてこの検査を実行してください。既存の異なる指示がある場合は内容を確認し、他の指示を削除せずに統合します。

新しい環境にも自動配置するには、リポジトリの取得後にこのコマンドを実行するよう環境の起動処理を設定する必要があります。スクリプトの追加だけではその設定やパーソナル指示は変更されません。

## 作品一覧

- [Gully Boy（2019）](movies/Gully-Boy-2019/)：[台詞集](movies/Gully-Boy-2019/dialogues/dialogue.md)・[Apna Time Aayega](movies/Gully-Boy-2019/songs/Apna-Time-Aayega.md)
- [3 Idiots（2009）](movies/3-Idiots-2009/)：[台詞集](movies/3-Idiots-2009/dialogues/dialogue.md)・[Aal Izz Well](movies/3-Idiots-2009/songs/Aal-Izz-Well.md)・[Give Me Some Sunshine](movies/3-Idiots-2009/songs/Give-Me-Some-Sunshine.md)・[Zoobi Doobi](movies/3-Idiots-2009/songs/Zoobi-Doobi.md)
- [Baazigar（1993）](movies/Baazigar-1993/)：[台詞集](movies/Baazigar-1993/dialogues/dialogue.md)・[Baazigar O Baazigar](movies/Baazigar-1993/songs/Baazigar-O-Baazigar.md)・[Kitabein Bahut Si](movies/Baazigar-1993/songs/Kitabein-Bahut-Si.md)・[Yeh Kaali Kaali Aankhen](movies/Baazigar-1993/songs/Yeh-Kaali-Kaali-Aankhen.md)
- [Bajrangi Bhaijaan（2015）](movies/Bajrangi-Bhaijaan-2015/)：[Aaj Ki Party](movies/Bajrangi-Bhaijaan-2015/songs/Aaj-Ki-Party.md)・[Chicken Kuk-Doo-Koo](movies/Bajrangi-Bhaijaan-2015/songs/Chicken-Kuk-Doo-Koo.md)・[Selfie Le Le Re](movies/Bajrangi-Bhaijaan-2015/songs/Selfie-Le-Le-Re.md)・[Tu Jo Mila](movies/Bajrangi-Bhaijaan-2015/songs/Tu-Jo-Mila.md)
- [Dangal（2016）](movies/Dangal-2016/)：[台詞集](movies/Dangal-2016/dialogues/dialogue.md)・[Haanikaarak Bapu](movies/Dangal-2016/songs/Haanikaarak-Bapu.md)・[Dangal (Title Track)](movies/Dangal-2016/songs/Dangal-Title-Track.md)・[Dhaakad](movies/Dangal-2016/songs/Dhaakad.md)
- [Dhurandhar（2025）](movies/Dhurandhar-2025/)：[台詞集](movies/Dhurandhar-2025/dialogues/dialogue.md)・[Dhurandhar - Title Track](movies/Dhurandhar-2025/songs/Dhurandhar-Title-Track.md)・[Gehra Hua](movies/Dhurandhar-2025/songs/Gehra-Hua.md)
- [Kabhi Khushi Kabhie Gham（2001）](movies/Kabhi-Khushi-Kabhie-Gham-2001/)：[台詞集](movies/Kabhi-Khushi-Kabhie-Gham-2001/dialogues/dialogue.md)・[Bole Chudiyan](movies/Kabhi-Khushi-Kabhie-Gham-2001/songs/Bole-Chudiyan.md)・[Suraj Hua Maddham](movies/Kabhi-Khushi-Kabhie-Gham-2001/songs/Suraj-Hua-Maddham.md)
- [Kuch Kuch Hota Hai（1998）](movies/Kuch-Kuch-Hota-Hai-1998/)：[Saajanji Ghar Aaye](movies/Kuch-Kuch-Hota-Hai-1998/songs/Saajanji-Ghar-Aaye.md)
- [Sholay（1975）](movies/Sholay-1975/)：[台詞集](movies/Sholay-1975/dialogues/dialogue.md)・[कितने आदमी थे?](movies/Sholay-1975/dialogues/Kitne-Aadmi-The.md)・[Yeh Dosti Hum Nahin Todenge](movies/Sholay-1975/songs/Yeh-Dosti-Hum-Nahin-Todenge.md)・[Haan Jab Tak Hai Jaan](movies/Sholay-1975/songs/Haan-Jab-Tak-Hai-Jaan.md)・[Holi Ke Din](movies/Sholay-1975/songs/Holi-Ke-Din.md)・[Koi Haseena](movies/Sholay-1975/songs/Koi-Haseena.md)・[Mehbooba Mehbooba](movies/Sholay-1975/songs/Mehbooba-Mehbooba.md)
- [Hum Aapke Hain Kaun（1994）](movies/Hum-Aapke-Hain-Kaun-1994/)：[Didi Tera Devar Deewana](movies/Hum-Aapke-Hain-Kaun-1994/songs/Didi-Tera-Devar-Deewana.md)・[Joote De Do Paise Le Lo](movies/Hum-Aapke-Hain-Kaun-1994/songs/Joote-De-Do-Paise-Le-Lo.md)・[Pehla Pehla Pyar Hai](movies/Hum-Aapke-Hain-Kaun-1994/songs/Pehla-Pehla-Pyar-Hai.md)
- [Zindagi Na Milegi Dobara（2011）](movies/Zindagi-Na-Milegi-Dobara-2011/)：[Sooraj Ki Baahon Mein](movies/Zindagi-Na-Milegi-Dobara-2011/songs/Sooraj-Ki-Baahon-Mein.md)・[Señorita](movies/Zindagi-Na-Milegi-Dobara-2011/songs/Senorita.md)
- [Dilwale Dulhania Le Jayenge（1995）](movies/Dilwale-Dulhania-Le-Jayenge-1995/)：[台詞集](movies/Dilwale-Dulhania-Le-Jayenge-1995/dialogues/dialogue.md)・[मेरे ख़्वाबों में](movies/Dilwale-Dulhania-Le-Jayenge-1995/songs/Mere-Khwabon-Mein.md)・[हो गया है तुझको तो प्यार सजना](movies/Dilwale-Dulhania-Le-Jayenge-1995/songs/Ho-Gaya-Hai-Tujhko-To-Pyar-Sajna.md)・[मेहंदी लगा के रखना](movies/Dilwale-Dulhania-Le-Jayenge-1995/songs/Mehndi-Laga-Ke-Rakhna.md)・[तुझे देखा तो](movies/Dilwale-Dulhania-Le-Jayenge-1995/songs/Tujhe-Dekha-To.md)
- [Karz（1980）](movies/Karz-1980/)：[Om Shanti Om](movies/Karz-1980/songs/Om-Shanti-Om.md)・[Ek Hasina Thi](movies/Karz-1980/songs/Ek-Hasina-Thi.md)・[Dard-E-Dil](movies/Karz-1980/songs/Dard-E-Dil.md)・[Paisa Yeh Paisa](movies/Karz-1980/songs/Paisa-Yeh-Paisa.md)
- [ओम शांति ओम（2007）](movies/Om-Shanti-Om-2007/)：[台詞集](movies/Om-Shanti-Om-2007/dialogues/dialogue.md)・[आँखों में तेरी](movies/Om-Shanti-Om-2007/songs/Aankhon-Mein-Teri.md)・[दास्तान-ए-ओम शांति ओम](movies/Om-Shanti-Om-2007/songs/Dastaan-E-Om-Shanti-Om.md)・[धूम ताना](movies/Om-Shanti-Om-2007/songs/Dhoom-Taana.md)・[दीवानगी दीवानगी](movies/Om-Shanti-Om-2007/songs/Deewangi-Deewangi.md)
- [Gangs of Wasseypur（2012）](movies/Gangs-of-Wasseypur-2012/)：[台詞集](movies/Gangs-of-Wasseypur-2012/dialogues/dialogue.md)・[Ek Bagal Mein Chand Hoga](movies/Gangs-of-Wasseypur-2012/songs/Ek-Bagal-Mein-Chand-Hoga.md)・[Keh Ke Lunga](movies/Gangs-of-Wasseypur-2012/songs/Keh-Ke-Lunga.md)・[O Womaniya](movies/Gangs-of-Wasseypur-2012/songs/O-Womaniya.md)
