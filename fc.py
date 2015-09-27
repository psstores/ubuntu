# -*- coding: utf-8 -*-
import jieba
import os
import chardet
import codecs
jieba.add_word('自拍')
jieba.add_word('自拍杆')
jieba.add_word('自拍神器')
fs=open('t.txt','r')
fs_w=open('test.txt','w')
con=fs.read()
seg_list=jieba.cut(con,cut_all=True)
content=' '.join(seg_list)
print chardet.detect(content)
fs_w.write(content.encode('utf-8'))
fs.close()
fs_w.close()
print("="*40)
