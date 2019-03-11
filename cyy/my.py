import time
import wda

'''
我的页面,认证后期需要加上
修改手机号码
作品的点击事件/滑动事件/点赞/
'''

# c = wda.Client('http://localhost:8100')
c = wda.Client('http://192.168.0.129:8100')
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


def my(c ,s):
    # 开始执行'我的'下点击操作
    s(label='我的').click()
    print('点击我的')

    # 点击账户与安全
    time.sleep(2)
    print('点击设置')
    s(label='nav settings').click()
    time.sleep(2)

    # 账号与安全,在当前页面有多个label的value为一致的 需要后面修改
    s(name='账号与安全').click()
    print(s(name='账号与安全', index=0))
    '''
    time.sleep(2)
    s(label='手机号').click()
    time.sleep(2)
    # 然后不修改手机号码直接返回    后期需要修改这边的逻辑
    # 添加点击验证码,修改手机号码.完成修改手机号用例
    s(className='Button', label='获取验证码').click()   # 点击获取验证码
    time.sleep(2)
    s(className='TextField').set_text('1111')    # 点击并输入验证码
    time.sleep(2)
    s(className='Button', label='下一步').click()
    time.sleep(2)
    s(className='TextField').find_elements()[0].set_text('13666666666')  # 点击输入新手机号码
    time.sleep(2)
    s(className='Button', label='获取验证码').click()
    time.sleep(2)
    s(className='TextField').find_elements()[1].set_text('1111')   # 点击输入验证码
    time.sleep(2)
    s(className='Button', label='确认').click()
    time.sleep(2)
    hone = s(className='TextField').find_elements()[0].value
    print('当前修改的手机号是%s' % hone)
    title = s(className='StaticText').find_elements()[0].value
    print('当前修改的手机号:%s-----title:%s' % hone, title)
    print('手机号码修改成功')
    '''

    # 点击第三方登录     后期需要添加这边的逻辑
    s(label='微信').click()
    time.sleep(2)
    # 不登录点击返回
    s(label='取消').click()
    time.sleep(2)
    s(label='退出登录').click()
    time.sleep(2)
    s(label='QQ').click()
    time.sleep(2)
    # 不登录直接返回
    s(label='关闭').click()
    time.sleep(1)
    # 校验设置页面的'我的账号'有没有
    m = s(label='我的账号').click_exists(2)
    if m:
        print('我的账号title显示正常')
    else:
        print('title上找不到我的账号')
    # 返回设置页面
    s(label='设置').click()
    time.sleep(3)

    # 点击通用设置
    s(label='通用设置').click()
    time.sleep(2)
    s(className='Switch').find_elements()[0].click()   # 点击按钮,是否可用
    time.sleep(2)
    number = s(className='Switch').find_elements()[0].value
    time.sleep(2)
    titles = s(className='StaticText').find_elements()[0].value
    print('通用设置非wifi下自动播放能够正常点击,1打开,0关闭,当前是:%s-----title:%s' % (number, titles))
    print('通用设置测试通过')


    s(label='设置').click()
    time.sleep(2)
    # 点击意见反馈
    s(label='意见反馈').click()
    time.sleep(4)
    s.swipe(0.5, 100, 0.5, 500, 1)
    time.sleep(2)
    # 后面添加反馈操作
    s.swipe(0.5, 500, 0.5, 100, 1)
    time.sleep(2)
    s(label='设置').click()
    print('意见反馈中不做操作,直接返回')
    time.sleep(1)

    # 点击关于   可以用滑动事件,目前是没有的   后期添加滑动事件
    s(label='关于').click()
    time.sleep(2)
    number2 = s(className='StaticText').find_elements()[3].value
    print('当前的版本号是:%s' % number2)
    time.sleep(2)
    s(label='社区公约').click()
    time.sleep(5)
    s.swipe(0.5, 100, 0.5, 500, 1)
    time.sleep(2)
    s.swipe(0.5, 500, 0.5, 100, 1)
    time.sleep(2)
    s(label='关于').click()
    time.sleep(1)
    s(label='用户协议').click()
    time.sleep(4)
    s.swipe(0.5, 100, 0.5, 500, 1)
    time.sleep(2)
    s.swipe(0.5, 500, 0.5, 100, 1)
    time.sleep(2)
    s(label='关于').click()
    time.sleep(1)
    s(label='隐私政策').click()
    time.sleep(5)
    s.swipe(0.5, 100, 0.5, 500, 1)
    time.sleep(2)
    s.swipe(0.5, 500, 0.5, 100, 1)
    time.sleep(2)
    s(label='关于').click()
    time.sleep(1)
    s(label='设置').click()
    time.sleep(1)
    s(label='清除缓存').click()
    time.sleep(2)
    s(className='Button', label='确定').click()
    time.sleep(2)
    # 返回主页
    s(label='nav back').click()
    time.sleep(1)

    # 点击二维码
    s(label='nav qrCode').click()
    time.sleep(1)
    s(label='保存到本地').click()
    time.sleep(3)
    # s(label='nav qrCode').click()
    # time.sleep(1)
    s(label='btn close pop').click()
    time.sleep(1)

    # 点击分享
    s(label='nav share').click()
    time.sleep(2)
    s(label='nav cross').click()
    time.sleep(1)

    # 点击用户昵称
    s(label='农夫').click()
    time.sleep(2)
    s(label='取消').click()
    time.sleep(1)
    s(label='农夫').click()
    time.sleep(2)
    s(className='TextField', value='农夫').click()
    time.sleep(2)
    s(className='Button', label='清除文本').click()
    time.sleep(2)
    s(className='TextField', value='昵称').set_text('农夫')
    time.sleep(2)
    s(className='TextField', value='本宝宝还没想好写什么').set_text('帅气')
    time.sleep(2)
    s(className='Image', name='avatar-edit-mask').click()       # 点击更换头像
    time.sleep(2)
    s(className='Button', name='从相册选择').click()
    time.sleep(2)
    s(className='Cell').find_elements()[7].click()
    time.sleep(2)
    s(className='Button', name='editor toolbar check').click()     # 选择照片以后,点击✅使用该照片
    time.sleep(2)
    s(label='完成').click()
    time.sleep(2)

    s(className='Image', name='ico-profile-unverified').click()   # 点击身份认证
    time.sleep(2)
    print(s(className='StaticText', name='身份认证').exists)     # 查看身份认证的title是否存在
    s(className='StaticText', name='我是宠物主人').click()
    time.sleep(2)
    s(className='StaticText', name='帅').click()
    time.sleep(2)
    print(s(className='StaticText', name='我是宠物主人').exists)   # 这里返回的是认证页面title是否显示一致
    s(className='Image', name='cert-photo-mask').click()    # 点击上传合照
    time.sleep(2)
    s(className='Button', name='从相册选择').click()
    time.sleep(2)
    s(className='Cell').find_elements()[7].click()
    time.sleep(2)
    s(className='Button', name='提交').click()
    time.sleep(3)
    s(className='Button', name='知道了').click()
    time.sleep(2)
    print(s(className='StaticText', name='身份认证审核中').exists)   # 验证提交以后页面是否显示正常


    # 点击关注      页面还有别的关注,需要区分,需要做修改      这里使用 label 加 value 两个属性来确定这个 元素
    s(label='关注', value='关注').click()
    time.sleep(2)
    s(label='返回').click()
    time.sleep(1)
    s(label='关注', value='关注').click()
    time.sleep(2)
    s(label='农夫山').click()
    time.sleep(2)
    s(label='nav back').click()
    time.sleep(2)
    s(label='农夫山').click()
    time.sleep(2)
    s(label='nav share').click()
    time.sleep(2)
    s(label='nav cross').click()
    time.sleep(1)
    s(label='nav back').click()
    '''最后的时候需要关注当前用户,以便下一次测试可以直接使用'''
    time.sleep(2)
    s(label='互关注').click()  # 页面显示问题,开发在改
    time.sleep(2)
    s(label='取消').click()
    time.sleep(1)
    s(label='返回').click()
    time.sleep(2)

    # 点击粉丝
    s(label='粉丝').tap()
    time.sleep(2)
    s(label='关注').tap()
    time.sleep(2)
    s(label='互关注').tap()
    time.sleep(2)
    s(label='取消').tap()
    time.sleep(1)
    s(label='互关注').tap()
    time.sleep(2)
    s(label='确定').tap()
    time.sleep(2)
    s(label='柯小基11').tap()
    time.sleep(2)
    s(className='StaticText', label='+ 关注').tap()  # 对用户进行关注
    time.sleep(1)
    s(className='StaticText', label='已关注').tap()
    time.sleep(2)
    s(label='确定').tap()
    time.sleep(2)    # 确保恢复
    s(className='StaticText', label='关注').tap()  # 点击他人的关注跳转关注页
    time.sleep(2)
    print(s(className='Other', label='TA的关注').exists)  # 校验title 是否存在

    s(className='StaticText', label='关注').tap()  # 需要修改
    time.sleep(1)
    s(className='StaticText', label='关注').tap()
    time.sleep(2)
    # s(label='取消').tap()
    time.sleep(2)
    s(className='StaticText', label='已关注').tap()
    time.sleep(2)
    s(label='确定').tap()
    time.sleep(2)
    s(className='Button', label='返回').tap()
    time.sleep(1)
    s(label='粉丝').tap()
    time.sleep(2)
    s(className='StaticText', label='关注').tap()
    time.sleep(2)
    print(s(className='Other', label='TA的粉丝').exists)
    s(className='StaticText', label='已关注').tap()
    time.sleep(2)
    s(label='取消').tap()
    time.sleep(2)
    s(className='StaticText', label='已关注').tap()
    time.sleep(2)
    s(label='确定').tap()
    time.sleep(2)
    s(className='Button', label='返回').tap()
    time.sleep(2)
    s(label='获赞').tap()
    time.sleep(2)
    s(className='Button', label='确认').tap()
    time.sleep(2)
    s(className='Button', label='nav back').tap()
    time.sleep(2)
    s(className='Button', label='返回').tap()
    time.sleep(2)

    # 点击获赞
    s(label='获赞').click()
    time.sleep(2)
    s(label='确认').click()
    time.sleep(2)
    '''作品,赞过,收藏暂时不能点击,页面暂时不能用s.swipe实现滑动'''
    s(className='Cell').find_elements()[3].click()     # 赞过双瀑布ugc_list
    time.sleep(2)
    s(className='Cell').find_elements()[5].click()      # 第二个ugc详情页
    time.sleep(3)



if __name__ == '__main__':

    my(c ,s)

    from cyydemo.webagent.cyy.msg import message

    message.information(c, s)

    from cyydemo.webagent.cyy.index import indexs

    indexs.indexs(c, s)
