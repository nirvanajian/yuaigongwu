# -*- coding:utf-8 -*-
# 与癌共舞主题帖爬取

import urllib
import urllib2
import re
import string

class yuaigongwu():   
 
    
      
   def get_page_number(self):
       page_number = input('请输入你想查找的页数:'.decode('utf-8').encode('gbk'))
       return page_number  

   def get_html(self, page_number):
       
       try:
           response = urllib2.urlopen('http://www.yuaigongwu.com/forum-93-' + str(page_number) + '.html')
           html = response.read()
           
           return html
       except urllib2.URLError, e:
           if hasattr(e, "reason"):
            
               print u"连接失败，错误原因是：" , e.reason
               return None

   def get_content(self, page_number):
       html = self.get_html(page_number)
       pattern = re.compile(r'xst.*?>(.*?)</a>.*?uid=.*?c="1">(.*?)</a></cite>.*?span>(.*?)</span>.*?"xi2">(.*?)</a><em>',re.S)
       content = re.findall(pattern, html)
       return content
      

   def date_pattern():
       pattern1 = re.compile(r'<span .*?="')
       pattern2 = re.compile(r'">.*?&nbsp;')

   def get_result(self):
       number = self.get_page_number()
       for i in range(number):
           page_content = self.get_content(i)
           print("正在输出第" + str(i+1) + "页的内容:")
           for part in page_content[2]:
               print part

    
yuaigongwu1 = yuaigongwu()

yuaigongwu1.get_result()
