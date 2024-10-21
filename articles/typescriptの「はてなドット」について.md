# 概要
typescriptに`?.`という表現がある。
Google検索時には「typescript はてなドット」のようなサジェストが挙がる。
オプショナルチェーン(optional chaining)という記法で`null`や`undefined`の可能性があるプロパティにアクセスするときにとても便利。

# 参考
[オプショナルチェーン (optional chaining) | サバイバルTypeScript](https://typescriptbook.jp/reference/values-types-variables/object/optional-chaining)

# サンプル
次のように`undefined`な可能性のあるオブジェクト`hoge`に対して`fuga()`メソッドを呼び出すときに使える。
```ts
interface Hoge {
    fuga: () => void
}

const sample1 = (hoge: Hoge | undefined) => {
    hoge?.fuga() // undefinedの可能性のあるhogeからfuga()を呼び出す。
}
```

`?.`を使わずに`hoge.fuga()`と書いてしまうと`undefined.fuga()`の意味合いとなってしまいエラーとなる。
簡単に言えば次のif分を省略するために`?.`が使える。
```ts
const sample2 = (hoge: Hoge | undefined) => {
    if (hoge) {
        hoge.fuga()
    }
}
```
