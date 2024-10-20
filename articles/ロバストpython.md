# 概要
typescriptのようにコード内で使う型をうまく定義できるとVScodeなどのIDEで型推論など嬉しいことがある。
pythonには型定義にいくつかの書き方があり、紛らわしいものがあるためまとめる。

# 型定義の書き方
```py
variable: int = 1
```

# 種類
- プリミティブ
    - int
    - str
    - bool
    など
- ユーザー定義
    - dataclasses.dataclass
    - typing.TypedDict
    - typing.Protocol
    - class

- ライブラリ
    - pydantic.dataclasses.dataclass

# 性質
- 静的解析
- 実行時チェック
- 実体(`type()`)
- メソッドを持てるか
- ミュータブル/イミュータブル
