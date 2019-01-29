import time
import wda


# c = wda.Client('http://localhost:8100')
c = wda.Client('http://192.168.2.139:8100')

print('链接成功')
print(c)

#c.home()

s = c.session('com.dealuck.cyyapp')
time.sleep(3)

s(name='首页').click()
time.sleep(3)
# 下拉刷新操作,
# s.swipe_down()
# time.sleep(3)

# 点击首页tap 呆萌,成精,生活操作
s(name='关注').click()
time.sleep(3)
l = s(name='消息').click_exists()
if l:
    print(l)
    s(name='消息').click()

time.sleep(3)

m = s(name='我的').click_exists()
if m:
    print('这是我的模块 ')
    s(name='我的').click()
time.sleep(3)


# 获取当前屏幕的大小   window_size()   和    screenshot()两种方式获取不同的屏幕大小
# 获取元素的方法
'''
s(ID).exists   返回真或是假
s(id='value')
s(name='value')
s(text='name')
s(nameContains='')
s(label='Address')
s(labelContains='Addr')
s(name='value',index=1)  返回一组数据,可以用下标取值
s(className='Button',name='value',visible=True,labelContains='Addr')
s(text='value').find_elements()
s().tap()
s().click()
s().set_timeout(时间单位秒)
s().clear()   清除当前点内容
s().set_text(需要发送的数据)

# 点击我的页面text为农夫山泉
s(text='农夫山泉').click()

'''
s(text='农夫山泉').click()
time.sleep(2)
s(name='取消').click()
time.sleep(2)
lists=['首页','关注','消息','我的']
for i in lists:
    s(label=i).click()
    time.sleep(1)
s(label='首页').click()
time.sleep(2)


# 首页推荐tap无法获取.采用坐标点击事件
















s.close()





