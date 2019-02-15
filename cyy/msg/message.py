import time


def information(c,s):
    # 点击消息
    s(label='消息').click()
    time.sleep(3)
    print('开始执行消息页测试用例')
    # 点击赞,获取赞与被赞列表
    print('赞列表的点击操作')
    s(label='赞').click()
    time.sleep(3)
    s(label='农夫山泉').click()
    time.sleep(3)
    s(label='nav back').click()
    time.sleep(1)
    s(label='农夫山泉').click()
    time.sleep(3)
    s(label='nav share').click()
    time.sleep(2)
    s(label='nav cross').click()
    time.sleep(2)
    s(label='nav share').click()
    time.sleep(3)
    s(name='mine_share_qrcode', text='二维码').click()
    time.sleep(2)
    s(label='btn close pop').click()   # 不保存二维码
    time.sleep(2)
    s(label='nav share').click()
    time.sleep(2)
    s(name='mine_share_qrcode').click()    # 对于唯一的name   使用name也是可以定位到该页面的元素
    time.sleep(3)
    s(label='保存到本地').click()        # 保存二维码    在这个地方的时候有时候点击保存二维码以后   可能页面可能还存在
    time.sleep(3)
    s(label='btn close pop').click()  # 不保存二维码
    time.sleep(2)

    # 点击复制链接    完事以后页面停留在 用户页面
    s(label='nav share').click()
    time.sleep(2)
    s(name='share_link', text='复制链接').click()
    time.sleep(3)

    # 点击个人用户主页的关注和粉丝,赞
    s(label='关注').click()
    time.sleep(3)
    s(label='农夫').click()
    time.sleep(3)
    s(label='nav back', name='nav back').click()
    time.sleep(1)
    s(label='互关注').click()
    time.sleep(3)
    s(label='取消').click()
    time.sleep(2)
    s(label='互关注').click()
    time.sleep(2)
    s(label='确定', name='确定').click()
    time.sleep(2)
    s(label='返回').click()
    time.sleep(2)

    # 点击粉丝
    s(label='粉丝').click()
    time.sleep(3)
    s(label='返回').click()
    time.sleep(2)

    # 点击获赞
    s(label='获赞').click()
    time.sleep(2)
    s(label='确认').click()
    time.sleep(3)

    # 点击赞过 下,上拉刷新     页面暂时不能定位到这两个元素
    # 点击作品  下,上拉刷新
    s.swipe(100, 700, 100, 300)
    s.swipe(100, 700, 100, 300)
    s.swipe(100, 300, 100, 700)
    s.swipe(100, 300, 100, 700)
    s.swipe(100, 300, 100, 700)

    s.tap(305,355)    # 获取不到页面上的  赞过元素  使用坐标点击
    s.swipe(100, 700, 100, 300)
    s.swipe(100, 700, 100, 300)
    s.swipe(100, 300, 100, 700)
    s.swipe(100, 300, 100, 700)
    s.swipe(100, 300, 100, 700)




    s(label='nav back').click()
    time.sleep(1)
    s(label='nav back').click()
    time.sleep(1)
    s(label='消息').click()
    time.sleep(1)

    print('执行完毕')


    # 点击粉丝事件
    from cyydemo.webagent.cyy.public import publics
    publics.fs(s)




