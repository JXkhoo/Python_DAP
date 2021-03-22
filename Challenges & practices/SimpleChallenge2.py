# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 11:04:38 2020

@author: Khoo Jie Xuan
"""
def extract_hashtags(text): 
   
    hashtag_list = [] 
 
    for word in text.split(): 
        if word[0] == '#': 
            hashtag_list.append(word[0:]) 
            
    return hashtag_list
        
def extract_url(text): 
   
    url_list = [] 
 
    for word in text.split(): 
        if ((word[0] == 'h') and (word[1] == 't')and (word[2] == 't')and (word[3] == 'p') ) : 
            url_list.append(word[0:]) 
  
    return url_list
             
with open('data.txt') as openfileobject:
    index = 0
    for line in openfileobject:
        hashtag_found = extract_hashtags(line)
        url_found = extract_url(line)
        post_data = {index:{'post':line,'hashtag':hashtag_found,'url':url_found}}
        print()
        print(post_data[index]['post'])
        print(post_data[index]['hashtag'])
        if url_found:
            print(post_data[index]['url'])
            index = index+1
