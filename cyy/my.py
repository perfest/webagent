import time
import wda


# c = wda.Client('http://localhost:8100')
c = wda.Client('http://192.168.2.139:8100')
print('链接成功')
s = c.session('com.dealuck.cyyapp')
print('成功启动cyyapp')

def my(c,s):
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
    print(s(name='账号与安全',index=0))
    time.sleep(2)
    s(label='手机号').click()
    time.sleep(2)
    # 然后不修改手机号码直接返回    后期需要修改这边的逻辑
    s(label='我的账号').click()
    time.sleep(1)
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
    s(label='设置').click()
    print('通用设置wifi播放不做点击直接返回')
    time.sleep(2)

    # 点击意见反馈
    s(label='意见反馈').click()
    time.sleep(4)
    s(label='设置').click()
    print('意见反馈中不做操作,直接返回')
    time.sleep(1)

    # 点击关于   可以用滑动事件,目前是没有的   后期添加滑动事件
    s(label='关于').click()
    time.sleep(2)
    s(label='社区公约').click()
    time.sleep(5)
    s(label='关于').click()
    time.sleep(1)
    s(label='用户协议').click()
    time.sleep(4)
    s(label='关于').click()
    time.sleep(1)
    s(label='隐私政策').click()
    time.sleep(5)
    s(label='关于').click()
    time.sleep(1)
    s(label='设置').click()
    time.sleep(1)

    # 点击清除缓存     后期在做修改
    # s(label='清除缓存').click()
    # time.sleep(2)

    # 点击退出登录   后期在做更改
    # s(label='退出登录').click()
    # time.sleep(2)

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
    s(label='农夫山泉').click()
    time.sleep(2)
    s(label='取消').click()
    time.sleep(1)
    s(label='农夫山泉').click()
    time.sleep(2)
    # 获取昵称的位置,然后更改   先清除文本内容,在set.text    更改用户名字


    # s(name='avatar-edit-mask').click()  # 点击照片更换
    # time.sleep(2)
    # s(label='取消').click()   # 取消返回
    # time.sleep(2)
    s(label='完成').click()
    time.sleep(2)
    # 暂时不能点击头像,,,后期看能不能改

    # 点击身份认证     页面中没有找到身份认证的话    程序会报错
    # s(label='点击认证身份').click()
    # time.sleep(2)
    # s(label='返回').click()
    # time.sleep(1)

    # 点击关注      页面还有别的关注,需要区分,需要做修改      这里使用 label 加 value 两个属性来确定这个 元素
    s(label='关注', value='关注').click()
    time.sleep(2)
    s(label='返回').click()
    time.sleep(1)
    s(label='关注', value='关注').click()
    time.sleep(2)
    s(label='新一').click()
    time.sleep(2)
    s(label='nav back').click()
    time.sleep(2)
    s(label='新一').click()
    time.sleep(2)
    s(label='nav share').click()
    time.sleep(2)
    s(label='nav cross').click()
    time.sleep(1)
    s(label='nav back').click()
    time.sleep(2)
    s(label='互关注').click()                         # 页面显示问题,开发在改
    time.sleep(2)
    s(label='取消').click()
    time.sleep(1)
    s(label='互关注').click()
    time.sleep(2)
    s(label='确定').click()
    time.sleep(2)
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
    s(className='StaticText').find_elements()[2].tap()     # 点击第一个用户的昵称 跳转用户主页
    time.sleep(2)
    s(className='StaticText', label='+ 关注').tap()         # 对用户进行关注
    time.sleep(1)
    s(className='StaticText', label='关注').tap()          # 点击他人的关注跳转关注页
    time.sleep(2)
    print(s(className='Other', label='TA的关注').exists)      # 校验title 是否存在
    
    s(className='StaticText', label='关注').tap()
    time.sleep(1)
    s(className='StaticText', label='已关注').tap()
    time.sleep(2)
    s(label='取消').tap()
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
    s.swipe(100, 700, 100, 300)         # 向上滑动事件
    s.swipe(100, 700, 100, 300)
    s.swipe(100, 300, 100, 700)
    s.swipe(100, 300, 100, 700)
    s.swipe(100, 300, 100, 700)
    s.swipe_left()
    time.sleep(2)
    s.swipe(100, 700, 100, 300)
    s.swipe(100, 700, 100, 300)
    s.swipe(100, 300, 100, 700)
    s.swipe(100, 300, 100, 700)
    s.swipe(100, 300, 100, 700)
    s(className='Button', label='nav back').tap()
    time.sleep(2)
    s(className='Button', label='返回').tap()
    time.sleep(2)
    
    # 点击获赞
    s(label='获赞').click()
    time.sleep(2)
    s(label='确认').click()
    time.sleep(2)

    # 点击宠物卡片中,宠物的名字,获取宠物卡片
    # s(label='二狗子').click()
    # time.sleep(2)

    '''作品,赞过,收藏暂时不能点击'''
    # 点击作品获取作品的详情信息
    # s(label='小崽子?').click()
    # time.sleep(2)


if __name__ == '__main__':

    my(c,s)

    from cyydemo.webagent.cyy.index import indexs

    indexs.indexs(c,s)

    from cyydemo.webagent.cyy.msg import message

    message.information(c,s)




