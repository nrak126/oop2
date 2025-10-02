# 第01回レポート

## 作成者
- 学籍番号: K24142
- 氏名: 矢部大智

## 問1
utils.pyのlist_generator_function関数の引数にstr型の値を指定した．
list_generator_function関数では引数はcountという変数に代入されており，countが使われている20行目で問題が発生する．
utils.pyの27行目のrangeの第二引数で, count + 1が指定されているが，countはstr型であり，int型の1との足し算ができず，TypeErrorが発生する．
その結果，list_generator_function関数がTypeError例外を発生させ，エラー１が表示される．

## 問2
print_process関数内では 第一引数を使用して```list_generator_function```関数を実行し,実行結果と第二引数を比べ、等しくなければValueError例外を発生させる．
utils.pyのprint_process関数の第一引数に ```number + 1``` を指定しているが, print_process第二引数には```number```で生成したfizzbuzzのリストが指定されており, 第一引数を使用した```list_generator_function```の実行結果とは等しくならず, ValueError例外が発生する.
