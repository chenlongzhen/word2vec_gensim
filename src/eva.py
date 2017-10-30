import gensim


model_data= '../data/wiki.cn.text.vector' 
model = gensim.models.Word2Vec.load_word2vec_format(model_data, binary=False)
model.most_similar("queen")
