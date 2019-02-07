import requests

#urllib, requests, 两种http请求发送方法,requests 更适合人类使用
class HTTP:#之所以把这个get()方法封装在对象里, 是为了之后的扩展
    @staticmethod
    def get(url,return_json=True):
        r=requests.get(url)
        #restful needed!
        if r.status_code!=200:#这个可以作为正常流程下的特例处理情况(比较不错哦)
            return {} if return_json else ''
        return r.json() if return_json else r.text#用Python三元表达式可以有效降低代码行数
