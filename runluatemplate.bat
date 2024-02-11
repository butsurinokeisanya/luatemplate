lualatex luatemplate.tex
upbibtex luatemplate
upmendex -l -s myist.ist -o luatemplate.ind luatemplate.idx -g
lualatex luatemplate.tex
lualatex luatemplate.tex