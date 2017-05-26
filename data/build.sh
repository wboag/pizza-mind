
time wget http://text-machine.cs.uml.edu/willie/enwiki-20170320-pages-articles-multistream.xml.bz2

time bzip2 -c -d enwiki-20170320-pages-articles-multistream.xml.bz2 | awk '{print tolower($0);}' | perl wikifil.pl | bash normalize_text.sh | awk '{if (NF>1) print;}' > data.txt

