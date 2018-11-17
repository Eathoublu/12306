#  - coding:utf-8 -
#- - - - -Eathoublu
#- - - -Version 1.0
import re
import requests
import cookielib
import urllib2
import urllib
import json

import sys

reload(sys)

sys.setdefaultencoding('gbk')

cookie = cookielib.CookieJar()
handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

headers = {
'Referer':'https://kyfw.12306.cn/otn/login/init',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'

}

loginURL = urllib2.Request('https://kyfw.12306.cn/otn/login/init', headers=headers)
html = opener.open(loginURL).read()
# print html #did succeeded!

captchaURL = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand', headers=headers)
imgCaptcha = opener.open(captchaURL).read()
with open('captcha.png', 'wb')as img:
    img.write(imgCaptcha)
    img.close()
position = raw_input('>>>Give Me Positon(English Character):')
data = {
        'answer': position,
        'login_site': 'E',
        'rand': 'sjrand'
}
data = urllib.urlencode(data)
checkCaptcha = urllib2.Request('https://kyfw.12306.cn/passport/captcha/captcha-check', headers=headers, data=data)
isOK = opener.open(checkCaptcha).read()
print isOK #get it!
data_2 = {
'username':'{your username}',
'password':'{your password}',
'appid':'otn'

}
data_2 = urllib.urlencode(data_2)
loginRequest = urllib2.Request('https://kyfw.12306.cn/passport/web/login',headers=headers, data=data_2)
isSucceeded = opener.open(loginRequest).read()
print isSucceeded

headers_2 = {
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, br',
'Accept-Language':'zh-CN,zh;q=0.9',
'Cache-Control':'no-cache',
'Connection':'keep-alive',
'Host':'kyfw.12306.cn',
'If-Modified-Since':'0',
'Referer':'https://kyfw.12306.cn/otn/leftTicket/init',
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}
req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/init', headers=headers_2)
test = opener.open(req)
print cookie
secretStr = raw_input(">>>请输入火车的secretStr:")

data_01 ={
'secretStr': secretStr,
'tour_flag':'dc',
'purpose_codes':'ADULT',
'query_from_station_name':'沈阳',
'query_to_station_name':'哈尔滨',
'undefined':''
}
data_01 = urllib.urlencode(data_01)
req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest', headers=headers_2, data=data_01)
rs_01 = opener.open(req)
print rs_01.read()


# print 'haha'
# test = requests.post('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest', data=data_01, headers=headers_2,cookies=cookie)
# print test.text


# test = urllib2.urlopen('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest')
# print test.read()


req_test = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest', headers=headers_2)
rs_02 = opener.open(req_test)
print rs_02.read()









# with open('test.txt', 'wb') as f:
#     f.write(rs_01.read())
#     f.close()





















# 下面是查询的
# data_3 = {
# 'leftTicketDTO.train_date':'2018-03-30',
# 'leftTicketDTO.from_station':'SYT',
# 'leftTicketDTO.to_station':'HBB',
# 'purpose_codes':'ADULT'
# }
# data_3 = urllib.urlencode(data_3)




# print data_3
# searchForTicket = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/queryZ', data=data_3)
#
# canSee = opener.open(searchForTicket).read()
# print canSee
# canSee = requests.get('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-03-30&leftTicketDTO.from_station=SYT&leftTicketDTO.to_station=HBB&purpose_codes=ADULT')
# canSee.encoding = canSee.apparent_encoding
# print canSee.text
# jsonReader = json.load(str(canSee.text))
# print jsonReader["result"]
# data_4 = {
# 'secretStr':'WqpIfWXKb3xyqSNnS9kRvmz88Y5l7vG6MBtWWycmN+J9HHAUiIiGY/zsSzyWrlLpCUZFc30XvqUlwo3oGoimyvmaXmdVmfbi2oZIs74msVyO29Yy4bC5LWwhCFcabow0suEdsumE3qk9kuy/hlKDHhYwdi5wB8Xrau2qaBE6KR7sKsS5ZsiAjg1nop7C9g7VM8Q9r0/GvZ1vUtW30r2nur6nAuYN5XngYEXVspsT3DGoAtqWNP5mmBqvB3LQSURruxuPZIjlPgw=',
# 'train_date':'2018-03-30',
# 'back_train_date':'2018-03-02',
# 'tour_flag':'dc',
# 'purpose_codes':'ADULT',
# 'query_from_station_name':'沈阳',
# 'query_to_station_name':'哈尔滨',
# 'undefined':''
# }
# data_4 = urllib.urlencode(data_4)
# buyTicket = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest', headers=headers_2, data=data_4)
#
# for i in cookie:
#     print i
# # req = urllib2.Request('https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random=1520082058083&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=150f50e73a3642eb1524085b406ae2fe',headers=headers_2)
# # html = opener.open(req)
# req = requests.get('https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime?random=1520082058083&tourFlag=dc&_json_att=&REPEAT_SUBMIT_TOKEN=150f50e73a3642eb1524085b406ae2fe', params=headers_2, cookies=cookie)
# req.encoding = req.apparent_encoding
# print req.text





