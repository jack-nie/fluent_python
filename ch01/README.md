
	1. 在python2中，对object的继承需要显示的写为FrenchDeck(object); 但是在python3中这个关系是默认的。
	2. namedtuple是为了创建一些不需要方法的对象，比如数据库记录。
	3. 通过实现__getitem__和__len__，可以实现自有的序列类型。
	4. __repr__和__str__的区别在于后者是在调用str()的时候使用，或者使用print函数打印一个对象的时候使用，它返回的字符串对终端更友好。 如果没有__str__，但是解释器又需要调用的时候，会把__repr__作为一个替代。
	5. %和str.format的区别。

