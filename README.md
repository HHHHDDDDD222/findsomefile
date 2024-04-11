# findsomefile
## 运行环境
linux+python

## 功能
自动提取文件中存在的敏感信息
支持微信小程序反编译后的文件
1.自动递归检索文件夹中所有文件包含的url＜/br＞
2.自动递归检索文件夹中所有文件包含的domain＜/br＞
3.自动递归检索文件夹中所有文件包含的IP＜/br＞
4.自动递归检索文件夹中所有文件包含的API包括路径（这部分参考了findsomething等项目）＜/br＞
5.自动递归检索文件夹中所有文件的js文件＜/br＞
6.自动递归检索文件夹中所有文件的json文件＜/br＞
7.自动递归检索文件夹中所有文件的config文件＜/br＞
8.自动递归检索文件夹中所有文件的身份证信息＜/br＞
9.自动递归检索文件夹中所有文件的手机号＜/br＞
10.自动递归检索文件夹中所有文件的邮箱＜/br＞
11.自动递归检索文件夹中所有小程序敏感信息＜/br＞
包括acesstoken，AccessKeyId，AccessKeySecret，corpid，secret＜/br＞
12.对可能存在的hash进行提取，并返回所在文件路径＜/br＞

## 使用方法
需要使用运行在linux环境中
chmod +x findsomefile＜/br＞
chmod +x find_apipath.py＜/br＞
./findsomefile -l <folder>＜/br＞
