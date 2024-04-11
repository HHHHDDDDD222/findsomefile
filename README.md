# findsomefile
## 运行环境
linux+python

## 功能
自动提取文件中存在的敏感信息  
支持微信小程序解密反编译后的文件  
1.自动递归检索文件夹中所有文件包含的url  
2.自动递归检索文件夹中所有文件包含的domain  
3.自动递归检索文件夹中所有文件包含的IP  
4.自动递归检索文件夹中所有文件包含的API包括路径（这部分参考了findsomething等项目）  
5.自动递归检索文件夹中所有文件的js文件  
6.自动递归检索文件夹中所有文件的json文件  
7.自动递归检索文件夹中所有文件的config文件  
8.自动递归检索文件夹中所有文件的身份证信息  
9.自动递归检索文件夹中所有文件的手机号  
10.自动递归检索文件夹中所有文件的邮箱  
11.自动递归检索文件夹中敏感信息；（微信小程序敏感信息收集）如解密反编译后的pc微信小程序文件从中提取出敏感信息  
包括模糊搜索acesstoken，AccessKeyId，AccessKeySecret，corpid，secret等  
12.对可能存在的hash进行提取，并返回所在文件路径  
 
## 使用方法
需要使用运行在linux环境中  
chmod +x findsomefile   
chmod +x find_apipath.py  
./findsomefile -l <*folder*>  
