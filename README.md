# PJama

## Concept

PJama (ぱじゃま) は、ICTSCで利用するスコアサーバです。


## Installation

```bash
# チェックアウト
git clone git@github.com:ictsc/ictsc-score.git
cd ictsc-score
# パッケージのインストール
pip install -r requirements.txt
# 自動整形
pip install autopep8
wget https://raw.githubusercontent.com/chibiegg/git-autopep8/master/pre-commit -O .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

# 動作チェック
cd src
python manage.py migrate # DBの作成
python manage.py runserver # テストサーバの起動
```

## Getting Started

開発環境の構築については [ictsc-score Wiki](https://github.com/ictsc/ictsc-score/wiki) を参照してください。


## Documentation

https://github.com/ictsc/ictsc-score/wiki
