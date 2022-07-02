#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pickle
import pandas as pd   


def predicttopfive(user_name):
    output_list=[]
    sentiment_file=open('./pickle/model_sentiment.pkl','rb')
    sentiment_model=pickle.load(sentiment_file)

    user_recomm_file=open('./pickle/user_reccomendation.pkl','rb')
    user_recomm_model=pickle.load(user_recomm_file)

    tfidf_file=open('./pickle/tfidf_vector.pkl','rb')
    tfidf_model=pickle.load(tfidf_file)

    df_sentiment=pd.read_csv('./data/new_df.csv')

    original_df=pd.read_csv('./data/sample30.csv')

    if user_name in user_recomm_model.index:

        top_20=user_recomm_model.loc[user_name].sort_values(ascending=False)[:20]

        origin_df=pd.DataFrame(original_df[['id','name']]).drop_duplicates()
        product_df=pd.merge(top_20,origin_df,on='id')

        sentiment_df=pd.DataFrame(df_sentiment[['id','user_sentiment','reviews_combined']]).drop_duplicates()
        sent_product=pd.merge(product_df,sentiment_df,on='id')


        vect_tfidf=tfidf_model.transform(sent_product['reviews_combined'])

        sent_product['sentiment_predicted']=sentiment_model.predict(vect_tfidf)

        sent_product['predicted_score']=sent_product['sentiment_predicted'].replace(['positive','negative'],[1,0])

        positive_sentiment=sent_product.pivot_table(index='name',values='predicted_score',aggfunc='mean')
        positive_sentiment.sort_values(by='predicted_score',ascending=False,inplace=True)
        display_text="THE TOP 5 PRODUCTS RECOMMENDED FOR "+user_name.upper()
        output_list.append(display_text)
        output_list.append("\n")

        for prod in positive_sentiment.head(5).index:
            output_list.append(prod)
            
    else:
        display_text="Invalid username, Please enter an username present in the list"
        output_list.append(display_text)
            
    return output_list

