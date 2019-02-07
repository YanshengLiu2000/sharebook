from flask import jsonify, request

from app.forms.book import SearchForm
from app.web.blueprint import web
from app.libs.helper import is_isbn_or_keyword
from app.spider.sharebook_book import SharebookBook





@web.route('/book/search')
def search():
    """
        q: normal keyword and isbn
        page
        ?q=xxx&page=1
        Request/Response class!
        Request记录了HTTP的相关请求信息
    """
    #在用之前, 需要验证合法性!
    # q=request.args['q']#request.args类似字典,是字典的子类, 不可变字典,可以转化成普通的可变字典 a=request.args.to_dict()
    # # q 至少需要有一个字符, 对长度有限制
    # page=request.args['page']
    # 页数需要是正整数, 有最大值限制
    form =SearchForm(request.args)
    #验证层
    if form.validate():
        q=form.q.data.strip()
        page=form.page.data#从form里面取得的值会经过判断~触发default=1
        isbn_or_keyword=is_isbn_or_keyword(q)
        if isbn_or_keyword == 'isbn':
            result=SharebookBook.search_by_isbn(q)
        else:
            result=SharebookBook.search_by_keyword(q,page)#dict 需要序列化(json化)
            print('test', result['books'])
        return jsonify(result)#这个就是API啦~ 数据的json化就是API
    else:
        return jsonify(form.errors)
