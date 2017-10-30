#!/bin/bash

today=`date +"%Y%m%d"`
mkdir ./data/${today}
cd ./src

# get article
echo "[INFO] get article"
sh ./get_article_content.sh

# jieba seg
echo "[INFO] preprocess article"
python preprocess_words.py ../data/${today}/article ../data/${today}/preprocess_article
echo "[INFO] seg article"
python seg_words.py ../data/${today}/preprocess_article ../data/${today}/seg_article

# w2v
echo "[INFO] w2v article"
python train_w2v_model.py ../data/${today}/seg_article ../data/${today}/article.model ../data/${today}/article.vector

cd -
