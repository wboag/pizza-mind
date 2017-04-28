wget http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-pages-articles.xml.bz2
bzip2 -c -d enwiki-latest-pages-articles.xml.bz2 | awk '{print tolower($0);}' | perl wikifil.pl | bash normalize_text.sh | awk '{if (NF>1) print;}' > data.txt

