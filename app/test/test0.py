from flask import Flask, current_app



app=Flask(__name__)
ctx=app.app_context()
ctx.push()
a=current_app
d=current_app.config["DEBUG"]
print('test, d= ',d)
ctx.pop()
"""
    以上是with 语句的解释
    with语句可以用于实现了上下文协议的对象.
    上下文管理器
    只要实现了__enter__  ,  __exit__就可以成为上下文管理器
    
    比如说数据库的操作可以封装在with里面
    连接数据库和释放数据库都可以卸载__enter__ 和__exit__里面.
"""

with app.app_context():
    print('test2: ', current_app.config['DEBUG'])
print('END!')

class A:
    def __enter__(self):
        print('this is enter!')
        a=1
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        需要用这几个参数处理异常
        :param exc_type:
        :param exc_val:异常原因
        :param exc_tb:异常堆栈信息
        :return: True or False. 如果返回false, 在正常运行完exit后, with结束抛出异常就是里面发生的异常信息, True 没有
            默认返回None 或者说是False
        """
        if exc_tb:
            print("有异常!")
        else:
            print('没事')
        print('This is exit!')
        return True
        return False

    def query(self):
        print('This is query!')

with A() as obj_A:
    print('obj_A=',obj_A)
    pass
"""
这里obj_A里面是空, 什么都没有. obj_A 里面存储的是__enter__方法返回的值.

"""
with A() as resource:
    resource.query()
"""
 这就是资源的查询, 用上下文管理器
"""