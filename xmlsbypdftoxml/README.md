[pdftoxml](https://sourceforge.net/projects/pdf2xml/files/binaries/Win32%202.1/)に`-noImage -cutPages`オプションを付けて[xion.pdf](http://conlinguistics.org/arka/images/xion.pdf)を入力した結果が`xion.pdf.xml`と`xion.pdf.xml_data`で、`-noImage`だけのが`xion.pdf.onefile.xml`

ちなみに以下のエラーと警告が出た:
```
Syntax Error: Couldn't read xref table
Syntax Warning: PDF file is damaged - attempting to reconstruct xref table...
```

あと、ayakaフォントやkardinalフォントの使用箇所を洗ひ出す際に以下のやうな部分を見つけてしまひ、少なくともその目的には有用ではないデータが出力されてしまつてゐるかもしれない事が判明:
```
<TEXT width="315.916" height="10.557" id="p23_t26" x="56.424" y="488.136">
  <TOKEN sid="p23_s1497" id="p23_w43" font-name="ipa???c" bold="no" italic="no" font-size="9" font-color="#000000" rotation="0" angle="0" x="56.424" y="488.136" base="496.056" width="257.704" height="9">
  部屋を見回すと、壁に何かの紙が貼ってあるのに気付いた。上段に"mel
  </TOKEN>
  <TOKEN sid="p23_s1498" id="p23_w44" font-name="kardinal" bold="no" italic="no" font-size="9" font-color="#000000" rotation="0" angle="0" x="315.79" y="488.568" base="496.056" width="56.55" height="10.125">
  406"と書いてあ
  </TOKEN>
</TEXT>
<TEXT width="294.68" height="9" id="p23_t27" x="48.264" y="505.2">
  <TOKEN sid="p23_s1499" id="p23_w45" font-name="ipa???c" bold="no" italic="no" font-size="9" font-color="#000000" rotation="0" angle="0" x="48.264" y="505.2" base="513.12" width="294.68" height="9">
  り、その下では=や(や)という文字が若干緑色に光っている。これは何だろう。
  </TOKEN>
</TEXT>
```
（適宜改行とインデントを入れて`href`屬性を除去してある）
