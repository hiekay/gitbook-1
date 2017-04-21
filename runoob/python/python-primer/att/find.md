#Python find()方法


#描述
Python find() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。

#语法
find()方法语法：

```
str.find(str, beg=0, end=len(string))
```

#参数
- str -- 指定检索的字符串
- beg -- 开始索引，默认为0。
- end -- 结束索引，默认为字符串的长度。

#返回值
如果包含子字符串返回开始的索引值，否则返回-1。

#实例
以下实例展示了find()方法的实例：

```
#!/usr/bin/python

str1 = "this is string example....wow!!!";
str2 = "exam";

print str1.find(str2);
print str1.find(str2, 10);
print str1.find(str2, 40);
```

以上实例输出结果如下：

```
15
15
-1
```