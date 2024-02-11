# LuaTemplate
```
**********************************************************************%
  _               _____                    _       _
 | |   _   _  __ |_   _|__ _ __ ___  _ __ | | __ _| |_ ___
 | |  | | | |/ _` || |/ _ \ '_ ` _ \| '_ \| |/ _` | __/ _ \
 | |__| |_| | (_| || |  __/ | | | | | |_) | | (_| | ||  __/
 |_____\__,_|\__,_||_|\___|_| |_| |_| .__/|_|\__,_|\__\___|
**********************************************************************%
```
## Description
LuaTemplate は モダンなTeX [LuaLaTeX](https://www.luatex.org/) のテンプレートファイルである.
TeXの基本的な章節や図表番号の自動割り付けに加え, 
- ハイパーリンク参照とPDFしおり機能.
- BibTeXを用いた自動参考文献作成機能.
- プログラミング言語の構文カラーリング, 等幅フォント出力.
- アルゴリズムの構文カラーリング.
- 論文出力(article)に加え, 本(book)形式をサポート.
- 自動索引作成機能.


## Install
[TeX Live - Quick instal](https://tug.org/texlive/quickinstall.html)に従って TeX Liveをインストールする.

## Folder Structure
```
  luatemplate
   │  apsrev4-2ja.bst
   │  luatemplate.pdf
   │  luatemplate.tex
   │  mybib.bib
   │  myist.ist
   │  mysty.sty
   │  rmluatemplate.bat
   │  rmluatemplate.command
   │  runluatemplate.bat
   │  runluatemplate.command
   │
   ├─bib
   │  │  doi2bib.py
   │  │  mydoi.csv
   │  │
   │  └─doi2bib
   │      │  crossref.py
   │      │  __init__.py
   │      │
   │      └─bin
   │            doi2bib
   ├─code
   │      bayes.sce.txt
   │      template.py
   │      template.vba
   │
   └─img
          template.png
```

## USAGE
TeX Liveをインストールしているならば, ターミナル(Mac)はコマンドプロンプト(Windows)でluatemplateフォルダ(luatemplate.texが入ったフォルダ)へ移動し,
次のコマンドを順次実行すれば参考文献・索引付きのPDFを生成することができる.
```
1) lualatex luatemplate.tex
2) runluatemplate.bat または runluatemplate.command
           (Windows)                   (MaC)
3) rmluatemplate.bat
```
runluatemplateは参考文献作成(upbibtex)と索引作成(upmendex)を行うバッチファイルである. rmluatemplateは不要な中間ファイルを消去するバッチファイルである.
(2)と(3)はファイルをダブルクリックしても実行できる.

## 索引
索引は本文中で英語であれば\index{lualatex}, 日本語であれば\index{るあらてっくす@ルアラテックス}のように記載すればrunluatemplateの索引作成(upmendex)によって
自動で索引を生成することができる.

- myist.istファイル
istファイルは索引の形式を指定する数行のファイルである. 下記の内容を変更することによって若干のスタイルの変更を行うことができる. 
"""
headings_flag 1
heading_prefix "{\\bfseries \\scalebox{1}{【"
heading_suffix "】}}\\nopagebreak\n"
delim_0 "\\dotfill"
delim_1 "\\dotfill"
delim_2 "\\dotfill"
letter_head      2
symhead_positive "\\symbolindexname"
"""

## 参考文献
本文中で\cite{Plumer_1988}のように記述する.

luatemplate.texファイルの末尾に次のように記載された箇所がある.
```
\bibliographystyle{apsrev4-2ja}
\bibliography{mybib}
```
apsrev4-2jaはapsrev4-2ja.bst(bibtex style)ファイルの読み込み,
mybibはmybib.bibファイルの読み込みを行う.

mybibの作成方法について2通り紹介する. これらの方法によって出力したmybib.bibで既存のmybib.bibファイルを置き換える.
- doi2bib
pythonをインストール済みならターミナル(Mac)はコマンドプロンプト(Windows)で
```
pip install doi2bib
```
を実行する. luatemplate/bibフォルダに移動し, 
```
py doi2bib.py -c mydoi.csv --output mybib.bib
```
を実行する. ここでmydoi.csvは1列目にdoi, 2列以降は自由にコメントが記載され, 複数行にわたってdoiが列挙された次に示すような内容のファイルである. 
```
DOI,2列目以降はメモ
10.1103/PhysRevLett.45.712,Plumerの論文1備考
10.1103/PhysRevB.28.4489,Plumerの論文2備考
```
DOIのAPIを使ってbibが取得され, mybib.bibが出力される.

- Zotero
オープンソースソフト[Zotero](https://www.zotero.org/download/)でデスクトップアプリとアドオンをインストールする. ブラウザのアドオンボタンをクリックしてZoteroのボタンを表示させる. 適当な論文ページを開き, Zoteroアドオンボタンをクリックするとデスクトップアプリに保存される. Zoteroのデスクトップアプリで \[ファイル > ライブラリをエクスポート\]をクリックして余分なファイルの出力を避けるためチェックボックスはすべて外してからBibTeX形式でmybib.bib出力する. 

## texファイルの内容
### 章節
```
\chapter{ダミー章}
\section{ダミー節 \label{sec:1}}
\subsubsection{ダミー小節}
\paragraph{ダミーパラグラフ}
```
※ \label{sec:1}を1回以上使用しなければしおりが作成されない.

### フォント
```
\section{フォント}
\textbf{ボールド} 
\textit{Italic} 
\small{フォント小さい} 
\large{フォント大きい} 
\fbox{文字を囲む} 
\texttt{Typewriter} 
\textgt{ゴシック} 
\keytop{キートップ} 
```

### 枠
```
\section{枠}
\begin{tcolorbox}[colframe=black, colback=white,
        colbacktitle=blue, coltitle=white,
        fonttitle=\bfseries\sffamily,title=
        純粋な枠]
    わくわく
\end{tcolorbox}
```

```
\begin{breakbox}
    \begin{itemize}
        \item folder\\folder2
        \item folder\\folder3
        \item folder\\folder4
    \end{itemize}
\end{breakbox}
```

```
本書で用いるプログラムはかなり多く, 目まぐるしく変わる.
そこで円滑な進行を図るとともにその内容に遺漏がないように
Windows上での操作手順を逐一記述しておく.
料理のレシピに相当する.
以後, 本文書では次の表記
\begin{screen}
    \begin{table}[H]
        \centering
        \renewcommand{\arraystretch}{0.8}
        \begin{tabular}{ll}
            「・・・」              & : プルダウンメニュー(>は階層同士の区切り)              \\
            "・・・"              & : ダイアログやメニュー中の設定・チェック項目, 質問, 一般の文字列. \\
            \lbrack ・・・\rbrack & : ボタン.                               \\
            \textbf{ボールド書体}    & : マクロ, ファイル名.                        \\
            \keytop{・・・}       & : キートップ.                             \\
        \end{tabular}
        \renewcommand{\arraystretch}{1}
    \end{table}
\end{screen}
を採用するものと約束する. 特筆大書したい文を\textcolor{red}{赤文字}で表示した.
慣習に従い, "hoge" はファイル名から拡張子を除いた文字列(メタ構文変数)
を表すものと約束する.
```

### 箇条書き
```
\section{箇条書き}
\begin{itemize}
    \item 箇条書き
\end{itemize}
```
```
\begin{enumerate}
    \item 箇条書き
\end{enumerate}
```

### 参照
```
\section{参照}
\refFig{fig:template.png}\par
\refTable{table:1}\par
\refSec{sec:1}\par
\refEq{eq:1}\par
\refApd{apd:1}\par
\refCode{code:1}\par
\refAlgorithm{algorithm:1} \par
\hypertarget{square}{正方格子}\par
\hyperlink{square}{正方格子}\par
\href{http://hoge}{url}\par
\url{http://hoge}\par
\cite{Plumer_1988} \par
\cite{Plumer_1989} \par
脚注を付けたい箇所\footnote{これが脚注です.}.
```

### 図
{サイズ}{ファイル名}{キャプション}. 参照は\refFig{fig:template.png}とする.
```
\myfig{12}{template.png}{キャプションです.}
```

### 表
{ヘッダー}{内容}{キャプション}{ラベル}
```
\mytable{lcc}
{\textbf{1} & \textbf{1} & \textbf{1} \\ }
{\textbf{1} & 1  & 1  \\ }
{キャプション}
{table:1}
```

### ソースコード
ソースコードはcodeフォルダに入れたファイルを参照するように1行追加するだけで作成できる. PythonとVBAを実装した. プリアンブルでlanguageと予約語morekeywordsを指定すればその他の言語に対応することができる.

Python
```
\lstinputlisting[style=Python, caption = PythonによるFizzBuzzのコード.,label = code:1]{code/template.py}
```
VBA
```
\lstinputlisting[style=VBA, caption = VBAによるFizzBuzzのコード.,label = code:1]{code/template.vba}
```

### アルゴリズム
例に倣って作成する.
```
\begin{algorithm}
    \label{algorithm:1}
    \caption{Dynamic PCA}
    \Comment{$\theta_{\mathrm{exp}}$ is globally given,
        and initially set to $\infty$.}
    \Function{ExpandBasisIfInteresting($B$, $\Sigma$, $\vec{x}$)}{
        \If{$\var{loss} > \theta_{\mathrm{exp}}$}{
            $\var{loss} \assign
                \sqrt{\lVert \vec{x} \rVert^2 - \lVert \vec{x}^T B \rVert^2}$
            \Comment{By Pythagoras}
            $B, \Sigma \assign
                \FuncCall{Append}{$B$, $\Sigma$, $\vec{x}$}$\;
            $B \assign \FuncCall{GramSchmidt}{$B$}$\;
        }
        $\theta_{\mathrm{exp}} \assign
            \FuncCall{UpdateLoss}{$\theta_{\mathrm{exp}}$, \var{loss}}$\;
        \algorithmReturn{$B$, $\Sigma$}\;
    }
    \Function{PeriodicDecompose($B$, $\Sigma$)}{
        \If{\FuncCall{IsOneMinutePassed}{}}{
            $B, \Sigma \assign \FuncCall{PCA}{$B$, $\Sigma$}$\;
        }
        \algorithmReturn{$B$, $\Sigma$}\;
    }
    \Comment{The main function}
    \Function{DynPCA($B$, $\Sigma$, $\vec{x}$, $s$)}{
        $B, \Sigma \assign
            \FuncCall{ExpandBasisIfInteresting}{$B$, $\Sigma$, $\vec{x}$}$\;
        $\Sigma \assign
            \FuncCall{UpdateCovMatrix}{$B$, $\Sigma$, $\vec{x}$, $s$}$\;
        $B', \Sigma' \assign
            \FuncCall{PeriodicDecompose}{$B$, $\Sigma$}$\;
        \algorithmReturn{$B'$, $\Sigma'$}
    }
\end{algorithm}
```

### 付録
```
\chapter{付録タイトル \label{apd:1}}
\section{付録見出し}
```



### 奥付
本のタイトル、著者名、発行者、発行所、発行年月日などが記載されている部分を奥付と呼ぶ. texファイルの末尾を適宜修正する.
```
\begin{screen}
    {\Large Lua\LaTeX テンプレート 第1版} 定価はカバーに表示\\
    {\today 第1版}
    \begin{table}[H]
        \centering
        \renewcommand{\arraystretch}{0.8}
        \begin{tabular}{ll}
            著者 & 名前太郎 \\
               & 名前次郎 \\
        \end{tabular}
        \renewcommand{\arraystretch}{1}
    \end{table}
    ©2024<無題複写・転載を禁ず>
\end{screen}
```

### book → articleへの変更は次のように置換する.
```
\documentclass[11pt,a4paper, titlepage]{ltjsarticle}
\subsubsection → \subsubsubsection
\subsection → \subsubsection
\section → \subsection
\chapter → \section
```
小さい順に格下げ
### book → articleへの変更は次のように置換する.
```
\documentclass[11pt,a4paper, titlepage]{ltjsbook}
\section → \chapter
\subsection → \section
\subsubsection → \subsection
\subsubsubsection → \subsubsection
```
大きい順に格上げ.