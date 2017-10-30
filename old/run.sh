#!/bin/bash

# xml2text
# python ./src/process_wiki.py ./data/zhwiki-latest-pages-articles.xml.bz2  wiki.cn.text

# jieba seg
#python ./src/seg_words.py ./data/article ./data/articel_seg
#python preprocess_words.py ../data/article_test ../data/out

# drop space
# python ./src/drop_space.py ./data/seg_word.txt

# w2v
python ./src/train_w2v_model.py ./data/seg_out ./data/article.model ./data/article.vector
