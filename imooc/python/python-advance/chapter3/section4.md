#3-4 python之使用`__future__`
Python的新版本会引入新的功能，但是，实际上这些功能在上一个老版本中就已经存在了。要“试用”某一新的特性，就可以通过导入`__future__`模块的某些功能来实现。

例如，Python 2.7的整数除法运算结果仍是整数：

	>>> 10 / 3
	3
但是，Python 3.x已经改进了整数的除法运算，“/”除将得到浮点数，“//”除才仍是整数：

	>>> 10 / 3
	3.3333333333333335
	>>> 10 // 3
	3
要在Python 2.7中引入3.x的除法规则，导入`__future__`的division：

	>>> from __future__ import division
	>>> print 10 / 3
	3.3333333333333335
当新版本的一个特性与旧版本不兼容时，该特性将会在旧版本中添加到`__future__`中，以便旧的代码能在旧版本中测试新特性。

##任务
在Python 3.x中，字符串统一为unicode，不需要加前缀 u，而以字节存储的str则必须加前缀 b。请利用`__future__`的unicode_literals在Python 2.7中编写unicode字符串。

 

?不会了怎么办
使用`from __future__ import unicode_literals`将把Python 3.x的unicode规则带入Python 2.7中。

参考代码:

	from __future__ import unicode_literals
	s = 'am I an unicode?'
	print isinstance(s, unicode)