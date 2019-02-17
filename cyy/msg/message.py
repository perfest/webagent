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
    s(label='确定', name='确定').click()       # 1.1.0版本中这里有问题
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
    s(label='消息').click()
    time.sleep(1)

    print('执行完毕')


    # 点击粉丝事件
    from cyydemo.webagent.cyy.public import publics
    publics.fs(s)


    # 点击评论事件
    s(label='评论').click()
    time.sleep(1)
    s(label='农夫').click()
    time.sleep(1)
    s(className='TextView').set_text('你很帅气')
    time.sleep(2)
    s(label='发送').click()
    time.sleep(2)
    s(className='Button').find_elements()[2].click()    # 对第一个实现点赞
    time.sleep(1)
    s(label='评论').click()
    time.sleep(2)
    s(className='Image').find_elements()[0].click()     # 点击 第一个图片 实现跳转到用户主页
    time.sleep(2)
    # 跳转用户主页以后 在次点击一遍之前的用户主页的操作

    s(className='Image').find_elements()[1].click()    # 实现点击获取评论的内容
    time.sleep(2)
    s(label='评论').click()
    time.sleep(2)
    s(label='消息').click()
    time.sleep(2)
    s(className='Cell').find_elements()[4].click()          # 点击宠优优小助手
    time.sleep(2)
    s(className='Cell').find_elements()[0].click()          # 点击第一条信息
    time.sleep(10)
    s(label='宠优优小助手').click()                                  # 这步是返回上一步
    time.sleep(2)
    s(label='消息').click()                                       # 返回
    time.sleep(2)
    s(calssName='Cell').find_elements()[5].click()
    time.sleep(2)
    s(label='消息').click()            # 直接返回
    time.sleep(2)

    print('消息页点击事件执行完成')


