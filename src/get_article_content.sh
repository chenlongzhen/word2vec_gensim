#!/bin/bash

today=`date +"%Y%m%d"`
mkdir ./data/${today}

get_article="
select summary from stage.s_z01_articles;
"

get_content="
select atopiccontent from stage.s_t02_autotopiccontent;
"

get_topic="
select ttitle from stage.s_t02_autotopic;
"


hive -e "$get_article" > ../data/${today}/article
#hive -e "$get_content" > ../data/content
#hive -e "$get_topic" > ../data/topic
