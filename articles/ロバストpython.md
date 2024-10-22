# 概要
typescriptのようにコード内で使う型をうまく定義できるとVScodeなどのIDEで型推論など嬉しいことがある。
pythonには型定義にいくつかの方法があり、紛らわしいものがあるためまとめる。

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
    - `dataclasses.dataclass`
        - 基本的にはこの方法で定義するのが一番汎用性が高い。
        - classやTypedDictによく似ている。
        - 実体はdataclassとして定義したクラスのインスタンス。
    - `typing.TypedDict`
        - 辞書の型を定義できる。
        - メソッドを含められない。
        - 実体はdict。プロパティへのアクセスは`sample['property_a']`のようにする。
    - `typing.Protocol`
        - ダックタイピングをサポートするための型定義。
            - 例）ある関数の引数に`Protocol`として定義した型を指定すると必要なプロパティを持ったオブジェクトであれば何でも受け付ける。
    - `class`
        - いわゆる一般的なクラス。
        - `dataclass`と違って`__init__`を使って初期化する。
        - `dataclass`では表現できないような型としての制約を定義できる。
            - 例）必ず`property_a` > `property_b`が成り立つ
            - 例）`array_a`プロパティは文字列配列で、1つ目の要素は必ず`'first'`が入る
            - 上記のような制約を`__init__`で表現して違反する場合はエラーとするなど。

- ライブラリ
    - `pydantic.dataclasses.dataclass`
        - 実行時に型チェックできるのが特徴、これ以外の型定義は基本的に静的解析のための定義。
            - jsonファイルを読み込んで`TypedDict`型に代入するとき、`str`型が期待されているプロパティに`int`型や`bool`型を指定しても実行エラーは出ない（静的解析ではエラーがでる）
            - このような「一見検出されそうな実行エラーが出ない」現象は`dataclasses.dataclass`などでも同様。
        - python標準の`dataclasses.dataclass`に`pydantic`のバリデーション機能(実行時型チェック)を付加したようなイメージ
        - `pydantic.BaseModel`はより多機能で`dataclass`では表現できないような制約を定義できる。標準的な`class`にバリデーション機能を付加したようなイメージ。


# 性質
- 静的解析
- 実行時チェック
- 実体(`type()`)
- メソッドを持てるか
- ミュータブル/イミュータブル
