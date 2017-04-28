
time wget https://dumps.wikimedia.org/enwiki/20170101/enwiki-20170101-pages-articles-multistream.xml.bz2

time bzip2 -c -d enwiki-latest-pages-articles.xml.bz2 | awk '{print tolower($0);}' | perl wikifil.pl | bash normalize_text.sh | awk '{if (NF>1) print;}' > data.txt

