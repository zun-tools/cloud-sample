# cloud-sample

YouTube チャンネル「ずんだもんの実験道具箱」の「Claude Code入門（応用編）」の回で使ったサンプルです。クラウドセッション（`claude --cloud`）に投げる練習用の、小さな Python プロジェクトです。

## 入っているもの

- `calc.py` — 足し算と平均の関数
- `tests/test_calc.py` — pytest のテスト2本。`test_average` が落ちる状態にしてあります

## 試し方

```
git clone https://github.com/<自分のアカウント>/cloud-sample
cd cloud-sample
claude --cloud "pytest で落ちているテストを直して"
```

注意: クラウドは GitHub に push 済みの内容をクローンします。手元だけの変更は届きません。自分のアカウントへフォークかコピーして使ってください。

License: MIT
