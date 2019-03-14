
import time
import wda

'''
我的页面,认证后期需要加上
修改手机号码
作品的点击事件/滑动事件/点赞/
'''

# c = wda.Client('http://localhost:8100')
c = wda.Client('http://192.168.0.130:8100')
print('链接成功')
print(c.status())
# print(c.wait_ready())
time.sleep(2)
s = c.session('com.apple.mobilesafari')
# s.close()
print('启动app')

# s = c.session('com.dealuck.cyyapp')
# s = c.session('com.apple.mobilesafari')
print(s.orientation)
print('成功启动')
time.sleep(10)


if __name__ == '__main__':

    from cyydemo.webagent.cyy import my

    my.my(c, s)

    from cyydemo.webagent.cyy.msg import message

    message.information(c, s)
