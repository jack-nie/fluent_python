
   1. 可变序列： list, bytearray, array.array, collections.deque, memoryview
       不可变序列: tuple,str,[]bytes
       容器序列: list， tuple, collections.deque可以存放不同类型的数据
       扁平序列: str, butes, bytearray, memoryview, array.array只能容纳一种类型。
   2.  列表推导式 [i for i in xrange(1, 10)]
   3. 列表推导式的作用就是生成列表，如果要生成其它类型的序列，那么就要使用生成器。生成器表达式背后遵循了迭代器协议，可以诸葛的产出元素，而不是先建立一个完整的列表，然后再把这个列表传递到某个构造函数里。
   4. 元组不仅仅是不可变列表，还可以用于没有字段名字的记录。
   5. 元组拆包.
   6. 不要把可变对象放到元组里面，增量赋值不是一个原子操作。