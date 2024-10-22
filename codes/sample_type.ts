// 型エイリアス
type SampleFunc = (arg: string) => string

// インターフェース
// 1階層
interface SampleObj1 {
    sampleProperty1: SampleObj2
    samplePropertyFunc1: SampleFunc | undefined
    sampleMethod1: SampleFunc
    [key: string]: any
}
// 複数階層
interface SampleObj2 {
    data: {
        msg: string
    }
}

// クラス
class SampleDataclass implements SampleObj1{
    // プロパティ
    // 型定義のみ
    sampleProperty1: SampleObj2
    // 初期化のみ(型は推論される)
    sampleProperty2 = 'this is sample sampleProperty2'
    // 型定義と初期化
    sampleProperty3: string = 'this is sampleProperty3'

    constructor(str: string) {
        this.sampleProperty1 = {
            data: {
                msg: str
            }
        }
    }

    // プロパティ関数: インスタンスごとに関数が生成される。関数内でthisが使える。
    // 型定義のみ
    samplePropertyFunc1!: (arg: string) => string
    // 関数定義のみ
    samplePropertyFunc2 = (arg: string) => {
        return arg
    }
    // 型定義と関数定義
    samplePropertyFunc3: (arg: string) => string = (arg) => {
        return arg
    }

    // クラスメソッド: すべてのインスタンスが単一のメソッドを使う。メソッド内でthisが使えない。
    // 戻り値の型定義なし
    sampleMethod1(arg: string) {
        return arg
    }
    // 戻り値のの型定義あり
    sampleMethod2(arg: string): string {
        return arg
    }
}

const sampleInstance = new SampleDataclass('hello')
console.log(sampleInstance.sampleProperty3)
