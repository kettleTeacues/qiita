interface Hoge {
    fuga: () => void
}

const sample1 = (hoge: Hoge | undefined) => {
    hoge?.fuga()
}

const sample2 = (hoge: Hoge | undefined) => {
    if (hoge) {
        hoge.fuga()
    }
}
