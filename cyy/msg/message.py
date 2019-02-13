import time


def information(c,s):
    # 点击消息
    s(label='消息').click()
    time.sleep(3)
    print('开始执行消息页测试用例')
    # 点击赞,获取赞与被赞列表
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
    s(name='mine_share_qrcode',text='二维码').click()
    time.sleep(2)
    s(label='btn close pop').click()   # 不保存二维码
    time.sleep(2)
    s(label='nav share').click()
    time.sleep(2)
    s(name='mine_share_qrcode').click()    # 对于唯一的name   使用name也是可以定位到该页面的元素
    time.sleep(3)
    s(label='保存到本地').click()        # 保存二维码    在这个地方的时候有时候点击保存二维码以后   可能页面可能还存在
    time.sleep(3)

    # 点击复制链接    完事以后页面停留在 用户页面
    s(name='share_link').click()
    time.sleep(3)

    # 点击个人用户主页的关注和粉丝,赞
    s(label='关注').click()
    time.sleep(3)
    s(label='农夫').click()
    time.sleep(3)
    s(label='nav back').click()
    time.sleep(1)

    s(label='nav back').click()
    time.sleep(1)










    pass






























