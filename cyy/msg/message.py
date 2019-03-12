import time


def information(c,s):
    # 点击消息
    s(label='消息').click()
    time.sleep(3)
    msg1 = s(label='宠优优小助手').exists
    if msg1:
        print('点击消息页跳转正常,当前状态 --%s' % msg1)
    else:
        print('点击消息页跳转异常,当前状态 --%s' % msg1)
    time.sleep(2)

    # 点击赞,获取赞与被赞列表
    s(className='Cell').find_elements()[0].click()
    time.sleep(3)
    msg2 = s(label='赞').exists
    if msg2:
        print('点击赞跳转正常,当前状态 --%s' % msg2)
    else:
        print('点击赞跳转异常,当前状态 --%s' % msg2)
    time.sleep(2)

    s(className='Cell').find_elements()[0].click()  # 点击当前列表的第一个
    time.sleep(3)       # 查找元素时不建议使用xpath在锁定元素.性能太差
    msg3 = s(label='发送').exists
    if msg3:
        print('点击跳转ugc详情正常,当前状态 --%s' % msg3)
    else:
        print('点击跳转ugc详情异常,当前状态 --%s' % msg3)
    time.sleep(2)

    s(label='nav back').click()
    time.sleep(1)
    msg4 = s(label='赞').exists
    if msg4:
        print('点击返回跳转正常,当前状态 --%s' % msg4)
    else:
        print('点击跳转异常,当前状态 --%s' % msg4)
    time.sleep(2)

    s(label='农夫山泉').click()
    time.sleep(3)
    msg5 = s(label='获赞').exists
    if msg5:
        print('点击用户昵称跳转正常,当前状态 --%s' % msg5)
    else:
        print('点击用户昵称跳转异常,当前状态 --%s' % msg5)
    time.sleep(2)

    s(label='nav share').click()
    time.sleep(2)
    msg6 = s(label='分享到').exists
    if msg6:
        print('点击分享弹框正常,当前状态 --%s' % msg6)
    else:
        print('点击分弹框享异常,当前状态 --%s' % msg6)
    time.sleep(2)

    s(label='nav cross').click()
    time.sleep(2)
    msg7 = s(label='分享到').exists
    if msg7:
        print('点击X分享的弹框消失异常,当前状态 --%s' % msg7)
    else:
        print('点击X分享的弹框消失正常,页面消失无之前的元素返回False,当前状态 --%s' % msg7)
    time.sleep(2)

    s(label='nav share').click()
    time.sleep(3)
    msg8 = s(label='分享到').exists
    if msg8:
        print('点击分享弹框正常,当前状态 --%s' % msg8)
    else:
        print('点击分弹框享异常,当前状态 --%s' % msg8)
    time.sleep(2)

    s(name='mine_share_qrcode', text='二维码').click()
    time.sleep(2)
    msg9 = s(label='btn close pop').exists
    if msg9:
        print('点击二维码弹框正常,当前状态 --%s' % msg9)
    else:
        print('点击二维码弹框异常,当前状态 --%s' % msg9)
    time.sleep(2)

    s(label='btn close pop').click()   # 不保存二维码
    time.sleep(2)
    msg10 = s(label='btn close pop').exists
    if msg10:
        print('点击X二维码没消失,当前状态 --%s' % msg10)
    else:
        print('点击X二维码消失,上个页面的元素不存在False,当前状态 --%s' % msg10)
    time.sleep(2)
    print('10条用例执行完毕')

    s(label='nav share').click()
    time.sleep(2)
    s(name='mine_share_qrcode').click()    # 对于唯一的name   使用name也是可以定位到该页面的元素
    time.sleep(3)
    s(label='保存到本地').click()        # 保存二维码    在这个地方的时候有时候点击保存二维码以后   可能页面可能还存在
    time.sleep(3)
    s(label='btn close pop').click()
    time.sleep(1)
    # 点击复制链接    完事以后页面停留在 用户页面
    s(label='nav share').click()
    time.sleep(2)
    s(name='share_link', text='复制链接').click()
    msg11 = s(label='复制成功').exists
    if msg11:
        print('复制二维码成功,当前状态 --%s' % msg11)
    else:
        print('二维码复制失败,页可能页面弹框太快,当前状态 --%s' % msg11)
    time.sleep(2)

    # 点击个人用户主页的关注和粉丝,赞
    s(label='关注').click()
    time.sleep(3)
    msg12 = s(label='TA的关注').exists
    if msg12:
        print('他人页面点击关注,跳转成功,当前状态 --%s' % msg12)
    else:
        print('他人页面点击关注,跳转失败,当前状态 --%s' % msg12)
    time.sleep(2)                                                   #  有问题

    s(label='已关注').click()
    time.sleep(2)
    msg13 = s(label='确定').exists
    if msg13:
        print('点击已关注弹框正常,当前状态 --%s' % msg13)
    else:
        print('点击已关注弹框失败,当前状态 --%s' % msg13)
    time.sleep(2)

    s(label='取消', name='取消').click()       # 1.1.0版本中这里有问题
    time.sleep(2)
    msg14 = s(label='确定').exists
    if msg14:
        print('点击取消弹框消失失败,当前状态 --%s' % msg14)
    else:
        print('点击取消弹框消失成功,当前状态 --%s' % msg14)
    time.sleep(2)

    s(label='已关注').click()
    time.sleep(2)
    s(label='确认', name='确认').click()
    time.sleep(2)
    s(label='农夫山').click()
    time.sleep(2)
    msg15 = s(label='+ 关注').exists
    if msg15:
        print('点击确认取消关注成功,当前状态 --%s' % msg15)
    else:
        print('点击确认取消关注失败,当前状态 --%s' % msg15)
    time.sleep(2)

    s(label='+ 关注').click()
    time.sleep(2)
    msg16 = s(label='已关注').exists
    if msg16:
        print('msg16成功,当前状态 --%s' % msg16)
    else:
        print('msg16失败,当前状态 --%s' % msg16)
    time.sleep(2)

    s(label='nav back').click()
    time.sleep(1)
    s(label='返回').click()
    time.sleep(2)
    msg17 = s(label='农夫山泉').exists
    if msg17:
        print('msg17成功,当前状态 --%s' % msg17)
    else:
        print('msg17失败,当前状态 --%s' % msg17)
    time.sleep(2)

    # 点击粉丝
    s(label='粉丝').click()
    time.sleep(3)
    msg18 = s(label='TA的粉丝').exists
    if msg18:
        print('msg18成功,当前状态 --%s' % msg18)
    else:
        print('msg18失败,当前状态 --%s' % msg18)
    time.sleep(2)

    s(label='关注').click()
    time.sleep(2)
    msg19 = s(label='已关注').exists
    if msg19:
        print('msg19成功,当前状态 --%s' % msg19)
    else:
        print('msg19失败,当前状态 --%s' % msg19)
    time.sleep(2)

    s(label='已关注').click()
    time.sleep(2)
    msg20 = s(label='确定').exists
    if msg20:
        print('msg20成功,当前状态 --%s' % msg20)
    else:
        print('msg20失败,当前状态 --%s' % msg20)
    time.sleep(2)

    s(label='确定')
    time.sleep(2)
    s(className='Cell').find_elements()[0].click()
    time.sleep(2)
    msg21 = s(label='+ 关注').exists
    if msg21:
        print('msg21成功,当前状态 --%s' % msg21)
    else:
        print('msg21失败,当前状态 --%s' % msg21)
    time.sleep(2)

    s(label='nav back').click()
    time.sleep(1)
    s(label='返回').click()
    time.sleep(2)
    msg22 = s(label='这个宝宝太懒了~').exists
    if msg22:
        print('msg22成功,当前状态 --%s' % msg22)
    else:
        print('msg22失败,当前状态 --%s' % msg22)
    time.sleep(2)

    # 点击获赞
    s(label='获赞').click()
    time.sleep(2)
    msg23 = s(label='确认').exists
    if msg23:
        print('msg23成功,当前状态 --%s' % msg23)
    else:
        print('msg23失败,当前状态 --%s' % msg23)
    time.sleep(2)

    s(label='确认').click()
    time.sleep(3)
    msg24 = s(label='确认').exists
    if msg24:
        print('msg24成功,当前状态 --%s' % msg24)
    else:
        print('msg24失败,当前状态 --%s' % msg24)
    time.sleep(2)

    s(className='ScrollView').click()   # 切换到赞过双瀑布列表下
    time.sleep(2)

    s(label='nav back').click()
    time.sleep(1)
    s(label='消息').click()
    time.sleep(1)
    msg25 = s(label='评论').exists
    if msg25:
        print('msg25成功,当前状态 --%s' % msg25)
    else:
        print('msg25失败,当前状态 --%s' % msg25)
    time.sleep(2)

    # 点击评论事件
    s(label='评论').click()
    time.sleep(1)
    msg26 = s(label='评论').exists
    if msg26:
        print('msg26成功,当前状态 --%s' % msg26)
    else:
        print('msg26失败,当前状态 --%s' % msg26)
    time.sleep(2)

    s(label='农夫山泉').click()          # 跳转评论的详情页
    time.sleep(1)
    msg27 = s(label='分享').exists
    if msg27:
        print('msg27成功,当前状态 --%s' % msg27)
    else:
        print('msg27失败,当前状态 --%s' % msg27)
    time.sleep(2)

    s(xpath='//XCUIElementTypeStaticText[@name="说点什么吧..."][1]').set_text('你很帅气')
    time.sleep(2)
    msg28 = s(label='你很帅气').exists
    if msg28:
        print('msg28成功,当前状态 --%s' % msg28)
    else:
        print('msg28失败,当前状态 --%s' % msg28)
    time.sleep(2)

    s(label='发送').click()
    msg29 = s(label='评论成功').exists
    if msg29:
        print('msg29执行成功,当前状态 --%s' % msg29)
    else:
        print('msg29执行失败,当前状态 --%s' % msg29)
    time.sleep(2)

    s(label='明明可以靠脸吃饭，偏偏要靠智商').click()
    msg30 = s(label='参与').exists
    if msg30:
        print('msg30执行成功,当前状态 --%s' % msg30)
    else:
        print('msg30执行失败,当前状态 --%s' % msg30)
    time.sleep(2)

    s(label='参与').click()
    msg31 = s(label='拍视频').exists
    if msg31:
        print('msg31执行成功,当前状态 --%s' % msg31)
    else:
        print('msg31执行失败,当前状态 --%s' % msg31)
    time.sleep(2)

    s(label='相册').click()
    msg32 = s(label='下一步').exists
    if msg32:
        print('msg32执行成功,当前状态 --%s' % msg32)
    else:
        print('msg32执行失败,当前状态 --%s' % msg32)
    time.sleep(2)

    s(label='c close bk').click()
    msg33 = s(label='浏览').exists
    if msg33:
        print('msg33执行成功,当前状态 --%s' % msg33)
    else:
        print('msg33执行失败,当前状态 --%s' % msg33)
    time.sleep(2)

    s(label='nav back').click()
    msg34 = s(label='分享').exists
    if msg34:
        print('msg34执行成功,当前状态 --%s' % msg34)
    else:
        print('msg34执行失败,当前状态 --%s' % msg34)
    time.sleep(2)

    print('34条用例执行完毕')

    '''
    s(label='评论').click()
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
    s(className='Cell').find_elements()[5].click()
    time.sleep(2)
    s(label='消息').click()            # 直接返回
    time.sleep(2)

    print('消息页点击事件执行完成')
    '''

