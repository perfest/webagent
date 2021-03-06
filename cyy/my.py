import time

def my(c ,s):
    # 开始执行'我的'下点击操作
    s(label='我的').click()
    print('点击我的')
    my1 = s(label='点击认证身份').exists
    if my1:
        print('点击我的成功,当前状态 --%s' % my1)
    else:
        print('点击我的失败,当前状态 --%s' % my1)
    time.sleep(2)

    # 点击账户与安全
    time.sleep(2)
    print('点击设置')
    s(label='nav settings').click()
    time.sleep(2)
    my2 = s(label='退出登录').exists
    if my2:
        print('点击设置跳转成功,当前状态 --%s' % my2)
    else:
        print('点击设置跳转失败,当前状态 --%s' % my2)
    time.sleep(2)

    # 账号与安全,在当前页面有多个label的value为一致的 需要后面修改
    s(name='账号与安全').click()
    time.sleep(1)
    my3 = s(label='我的账号').exists
    if my3:
        print('点击账号安全跳转成功,当前状态 --%s' % my3)
    else:
        print('点击账号安全跳转失败,当前状态 --%s' % my3)
    time.sleep(2)
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
    my4 = s(label='发送').exists
    if my4:
        print('点击微信跳转成功,当前状态 --%s' % my4)
    else:
        print('点击微信跳转失败,当前状态 --%s' % my4)
    time.sleep(2)

    # 不登录点击返回
    s(label='取消').click()
    time.sleep(2)
    my5 = s(label='取消后将退出本次登录').exists
    if my5:
        print('成功,当前状态 --%s' % my5)
    else:
        print('失败,当前状态 --%s' % my5)
    time.sleep(2)

    s(label='退出登录').click()
    time.sleep(2)
    my6 = s(label='第三方账号绑定').exists
    if my6:
        print('返回成功,当前状态 --%s' % my6)
    else:
        print('返回失败,当前状态 --%s' % my6)
    time.sleep(2)

    s(label='QQ').click()
    time.sleep(2)
    my7 = s(label='登录').exists
    if my7:
        print('跳转成功,当前状态 --%s' % my7)
    else:
        print('跳转失败,当前状态 --%s' % my7)
    time.sleep(2)

    # 不登录直接返回
    s(label='关闭').click()
    time.sleep(1)
    # 校验设置页面的'我的账号'有没有
    my8 = s(label='我的账号').click_exists(2)
    if my8:
        print('我的账号title显示正常')
    else:
        print('title上找不到我的账号')

    # 返回设置页面
    s(label='设置').click()
    time.sleep(3)
    my9 = s(label='清除缓存').exists
    if my9:
        print('跳转成功,当前状态 --%s' % my9)
    else:
        print('跳转失败,当前状态 --%s' % my9)
    time.sleep(2)

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
    my11 = s(label='退出登录').exists
    if my11:
        print('my11执行成功,当前状态 --%s' % my11)
    else:
        print('my11执行失败,当前状态 --%s' % my11)
    time.sleep(2)

    # 点击意见反馈
    s(label='意见反馈').click()
    time.sleep(4)
    my12 = s(label='意见反馈').exists
    if my12:
        print('my11执行成功,当前状态 --%s' % my12)
    else:
        print('my11执行失败,当前状态 --%s' % my12)
    time.sleep(2)

    s.swipe(0.5, 100, 0.5, 500, 1)
    time.sleep(2)
    # 后面添加反馈操作
    s.swipe(0.5, 500, 0.5, 100, 1)
    time.sleep(2)
    s(label='设置').click()
    print('意见反馈中不做操作,直接返回')
    time.sleep(1)
    my13 = s(label='关于').exists
    if my13:
        print('my13执行成功,当前状态 --%s' % my13)
    else:
        print('my13执行失败,当前状态 --%s' % my13)
    time.sleep(2)

    # 点击关于   可以用滑动事件,目前是没有的   后期添加滑动事件
    s(label='关于').click()
    time.sleep(2)
    my14 = s(label='用户协议').exists
    if my14:
        print('my14执行成功,当前状态 --%s' % my14)
    else:
        print('my14执行失败,当前状态 --%s' % my14)
    time.sleep(2)

    number2 = s(className='StaticText').find_elements()[3].value
    print('当前的版本号是:%s' % number2)
    time.sleep(2)
    s(label='社区公约').click()
    time.sleep(5)
    my15 = s(label='宠优优社区公约').exists
    if my15:
        print('my15执行成功,当前状态 --%s' % my15)
    else:
        print('my15执行失败,当前状态 --%s' % my15)
    time.sleep(2)

    s.swipe(0.5, 100, 0.5, 500, 1)
    time.sleep(2)
    s.swipe(0.5, 500, 0.5, 100, 1)
    time.sleep(2)
    s(label='关于').click()
    time.sleep(1)
    my16 = s(label='隐私政策').exists
    if my16:
        print('my16执行成功,当前状态 --%s' % my16)
    else:
        print('my16执行失败,当前状态 --%s' % my16)
    time.sleep(2)

    s(label='用户协议').click()
    time.sleep(4)
    my17 = s(label='宠优优用户注册协议').exists
    if my17:
        print('my17执行成功,当前状态 --%s' % my17)
    else:
        print('my17执行失败,当前状态 --%s' % my17)
    time.sleep(2)

    s.swipe(0.5, 100, 0.5, 500, 1)
    time.sleep(2)
    s.swipe(0.5, 500, 0.5, 100, 1)
    time.sleep(2)
    s(label='关于').click()
    time.sleep(1)
    my18 = s(label='社区公约').exists
    if my18:
        print('my18执行成功,当前状态 --%s' % my18)
    else:
        print('my18执行失败,当前状态 --%s' % my18)
    time.sleep(2)

    s(label='隐私政策').click()
    time.sleep(5)
    my19 = s(label='宠优优用户隐私政策').exists
    if my19:
        print('my19执行成功,当前状态 --%s' % my19)
    else:
        print('my19执行失败,当前状态 --%s' % my19)
    time.sleep(2)

    s.swipe(0.5, 100, 0.5, 500, 1)
    time.sleep(2)
    s.swipe(0.5, 500, 0.5, 100, 1)
    time.sleep(2)
    s(label='关于').click()
    time.sleep(1)
    my20 = s(label='关于').exists
    if my20:
        print('my20执行成功,当前状态 --%s' % my20)
    else:
        print('my20执行失败,当前状态 --%s' % my20)
    time.sleep(2)

    s(label='设置').click()
    time.sleep(1)
    my21 = s(label='清除缓存').click_exists(5)
    time.sleep(2)
    if my21:
        print('my21执行成功,当前状态 --%s' % my21)
    else:
        print('my21执行失败,当前状态 --%s' % my21)
    time.sleep(2)

    s(className='Button', label='确定').click()
    time.sleep(2)
    my22 = s(label='0.00 B').exists
    if my22:
        print('my22执行成功,当前状态 --%s' % my22)
    else:
        print('my22执行失败,当前状态 --%s' % my22)
    time.sleep(2)

    # 返回主页
    s(label='nav back').click()
    time.sleep(1)
    my23 = s(label='点击认证身份').exists
    if my23:
        print('my23执行成功,当前状态 --%s' % my23)
    else:
        print('my23执行失败,当前状态 --%s' % my23)
    time.sleep(2)

    # 点击二维码
    s(label='nav qrCode').click()
    time.sleep(1)
    my24 = s(label='保存到本地').click_exists(5)
    time.sleep(3)
    if my24:
        print('my24执行成功,当前状态 --%s' % my24)
    else:
        print('my24执行失败,当前状态 --%s' % my24)
    time.sleep(2)
    s(label='btn close pop').click()    #  模拟器中测试需要添加这行代码
    time.sleep(1)

    # 点击分享
    s(label='nav share').click()
    time.sleep(2)
    my25 = s(label='分享到').exists
    if my25:
        print('my25执行成功,当前状态 --%s' % my25)
    else:
        print('my25执行失败,当前状态 --%s' % my25)
    time.sleep(2)

    s(label='nav cross').click()
    time.sleep(1)
    my26 = s(label='首页').exists
    if my26:
        print('my26执行成功,当前状态 --%s' % my26)
    else:
        print('my26执行失败,当前状态 --%s' % my26)
    time.sleep(2)

    # 点击用户昵称
    s(label='农夫').click()
    time.sleep(2)
    my27 = s(label='编辑资料').exists
    if my27:
        print('my27执行成功,当前状态 --%s' % my27)
    else:
        print('my27执行失败,当前状态 --%s' % my27)
    time.sleep(2)

    s(label='取消').click()
    time.sleep(1)
    my28 = s(label='帅气').exists
    if my28:
        print('my28执行成功,当前状态 --%s' % my28)
    else:
        print('my28执行失败,当前状态 --%s' % my28)
    time.sleep(2)

    s(label='农夫').click()
    time.sleep(2)
    s(className='TextField', value='农夫').click()
    time.sleep(2)
    my29 = s(className='Button', label='清除文本').click_exists(5)
    if my29:
        print('my29执行成功,当前状态 --%s' % my29)
    else:
        print('my29执行失败,当前状态 --%s' % my29)
    time.sleep(2)

    s(className='TextField', value='昵称').set_text('农夫')
    time.sleep(2)
    my30 = s(className='TextField', value='农夫').exists
    if my30:
        print('my30执行成功,当前状态 --%s' % my30)
    else:
        print('my30执行失败,当前状态 --%s' % my30)
    time.sleep(2)

    s(className='TextField', value='帅气').set_text('\b\b')
    time.sleep(1)
    s(className='TextField', value='本宝宝还没想好写什么').set_text('帅气')
    time.sleep(2)
    my31 = s(className='Button', label='清除文本').exists
    if my31:
        print('my31执行成功,当前状态 --%s' % my31)
    else:
        print('my31执行失败,当前状态 --%s' % my31)
    time.sleep(2)

    s(className='TextField', value='点击设置地区').click()
    my32 = s(label='北京').click_exists(5)
    if my32:
        print('my32执行成功,当前状态 --%s' % my32)
    else:
        print('my32执行失败,当前状态 --%s' % my32)
    time.sleep(2)

    my33 = s(label='东城').click_exists(5)
    if my33:
        print('my33执行成功,当前状态 --%s' % my33)
    else:
        print('my33执行失败,当前状态 --%s' % my33)
    time.sleep(2)

    my34 = s(value='北京•东城').exists
    if my34:
        print('my34执行成功,当前状态 --%s' % my34)
    else:
        print('my34执行失败,当前状态 --%s' % my34)
    time.sleep(2)

    # 当前停留在用户资料的修改页面.上一步在 选择地址的这个地方
    s(className='TextField', value='男').click()
    my35 = s(label='女').click_exists()
    if my35:
        print('my35执行成功,当前状态 --%s' % my35)
    else:
        print('my35执行失败,当前状态 --%s' % my35)
    time.sleep(2)

    if s(className='TextField', value='女').value == '女':
        print('性别选择ok')
    else:
        print('选择无效')

    s(className='Image', name='avatar-edit-mask').click()      # 点击更换头像
    time.sleep(2)
    my36 = s(label='拍照').exists
    if my36:
        print('my36执行成功,当前状态 --%s' % my36)
    else:
        print('my36执行失败,当前状态 --%s' % my36)
    time.sleep(2)

    s(className='Button', name='从相册选择').click()
    time.sleep(2)
    s(className='Cell').find_elements()[7].click()
    time.sleep(2)
    my37 = s(label='裁剪').exists
    if my37:
        print('my37执行成功,当前状态 --%s' % my37)
    else:
        print('my37执行失败,当前状态 --%s' % my37)
    time.sleep(2)

    s(className='Button', name='editor toolbar check').click()     # 选择照片以后,点击✅使用该照片
    time.sleep(2)
    s(label='取消').click()
    time.sleep(2)
    my38 = s(label='首页').exists
    if my38:
        print('my38执行成功,当前状态 --%s' % my38)
    else:
        print('my38执行失败,当前状态 --%s' % my38)
    time.sleep(2)
    # s(label='完成').click()       点击完成以后.资料将被修改.下次再测需要维护代码
    # time.sleep(2)                 最后一次验收测试 点击完成

    s(className='Image', name='ico-profile-unverified').click()   # 点击身份认证
    time.sleep(2)
    my39 = s(className='StaticText', name='身份认证').exists     # 查看身份认证的title是否存在
    if my39:
        print('my39执行成功,当前状态 --%s' % my39)
    else:
        print('my39执行失败,当前状态 --%s' % my39)
    time.sleep(2)

    s(className='StaticText', name='我是宠物主人').click()
    time.sleep(2)
    my40 = s(className='StaticText', name='我的宠物').exists
    if my40:
        print('my40执行成功,当前状态 --%s' % my40)
    else:
        print('my40执行失败,当前状态 --%s' % my40)
    time.sleep(2)

    s(className='StaticText', name='帅').click()
    time.sleep(2)
    my41 = s(label='提交').exists
    if my41:
        print('my41执行成功,当前状态 --%s' % my41)
    else:
        print('my41执行失败,当前状态 --%s' % my41)
    time.sleep(2)

    s(className='Image', name='cert-photo-mask').click()    # 点击上传合照
    time.sleep(2)
    my42 = s(className='Button', name='从相册选择').exists
    if my42:
        print('my42执行成功,当前状态 --%s' % my42)
    else:
        print('my42执行失败,当前状态 --%s' % my42)
    time.sleep(2)

    s(className='Button', name='从相册选择').click()
    time.sleep(2)
    my10 = s(className='Button', name='取消').exists
    if my10:
        print('my10执行成功,当前状态 --%s' % my10)
    else:
        print('my10执行失败,当前状态 --%s' % my10)
    time.sleep(2)

    s(className='Cell').find_elements()[7].click()
    time.sleep(2)
    s(className='Button', name='提交').click()
    time.sleep(3)
    s(className='Button', name='知道了').click()
    time.sleep(2)
    my43 = s(className='StaticText', name='身份认证审核中').exists   # 验证提交以后页面是否显示正常
    if my43:
        print('my43执行成功,当前状态 --%s' % my43)
    else:
        print('my43执行失败,当前状态 --%s' % my43)
    time.sleep(2)

    # 点击关注      页面还有别的关注,需要区分,需要做修改      这里使用 label 加 value 两个属性来确定这个 元素
    s(label='关注', value='关注').click()
    time.sleep(2)
    my44 = s(label='我的关注').exists
    if my44:
        print('my44执行成功,当前状态 --%s' % my44)
    else:
        print('my44执行失败,当前状态 --%s' % my44)
    time.sleep(2)

    s(label='返回').click()
    time.sleep(1)
    my45 = s(label='ID: 17297747').exists
    if my45:
        print('my45执行成功,当前状态 --%s' % my45)
    else:
        print('my45执行失败,当前状态 --%s' % my45)
    time.sleep(2)

    s(label='关注', value='关注').click()
    time.sleep(2)
    s(label='农夫山').click()
    time.sleep(2)
    my46 = s(label='这个宝宝太懒了~').exists
    if my46:
        print('my46执行成功,当前状态 --%s' % my46)
    else:
        print('my46执行失败,当前状态 --%s' % my46)
    time.sleep(2)

    s(label='nav back').click()
    time.sleep(2)
    s(label='农夫山').click()
    time.sleep(2)
    s(label='nav share').click()
    time.sleep(2)
    my47 = s(label='分享到').exists
    if my47:
        print('my47执行成功,当前状态 --%s' % my47)
    else:
        print('my47执行失败,当前状态 --%s' % my47)
    time.sleep(2)

    s(label='nav cross').click()
    time.sleep(1)
    s(label='nav back').click()
    time.sleep(2)
    s(label='互关注').click()  # 页面显示问题,开发在改
    time.sleep(2)
    my48 = s(label='确定').exists
    if my48:
        print('my48执行成功,当前状态 --%s' % my48)
    else:
        print('my48执行失败,当前状态 --%s' % my48)
    time.sleep(2)

    s(label='取消').click()
    time.sleep(1)
    s(label='返回').click()
    time.sleep(2)

    # 点击粉丝
    s(label='粉丝').tap()
    time.sleep(2)
    my49 = s(label='我的粉丝').exists
    if my49:
        print('my49执行成功,当前状态 --%s' % my49)
    else:
        print('my49执行失败,当前状态 --%s' % my49)
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
    my50 = s(label='+ 关注').exists
    if my50:
        print('my50执行成功,当前状态 --%s' % my50)
    else:
        print('my50执行失败,当前状态 --%s' % my50)
    time.sleep(2)

    s(className='StaticText', label='关注').tap()  # 点击他人的关注跳转关注页
    time.sleep(2)
    my51 = s(className='NavigationBar', name='TA的关注').exists
    if my51:
        print('my51执行成功,当前状态 --%s' % my51)
    else:
        print('my51执行失败,当前状态 --%s' % my51)
    time.sleep(2)

    s(className='StaticText', label='关注').tap()  # 需要修改
    time.sleep(1)
    s(className='StaticText', label='已关注').tap()
    time.sleep(2)
    s(label='确定').tap()
    time.sleep(2)
    my52 = s(label='关注').exists
    if my52:
        print('my52执行成功,当前状态 --%s' % my52)
    else:
        print('my52执行失败,当前状态 --%s' % my52)
    time.sleep(2)

    s(className='Button', label='返回').tap()
    time.sleep(1)
    s(label='粉丝').tap()
    time.sleep(2)
    my53 = s(label='TA的粉丝').exists
    if my53:
        print('my53执行成功,当前状态 --%s' % my53)
    else:
        print('my53执行失败,当前状态 --%s' % my53)
    time.sleep(2)

    s(className='StaticText', label='关注').tap()
    time.sleep(2)
    s(className='StaticText', label='已关注').tap()
    time.sleep(2)
    s(label='确定').click()
    time.sleep(1)
    my54 = s(label='+ 关注').exists
    if my54:
        print('my54执行成功,当前状态 --%s' % my54)
    else:
        print('my54执行失败,当前状态 --%s' % my54)
    time.sleep(2)

    s(className='Button', label='返回').tap()
    time.sleep(2)
    s(label='获赞').tap()
    time.sleep(2)
    my55 = s(className='Button', label='确认').click_exists(5)
    time.sleep(1)
    if my55:
        print('my55执行成功,当前状态 --%s' % my55)
    else:
        print('my55执行失败,当前状态 --%s' % my55)
    time.sleep(2)

    s(className='Button', label='nav back').tap()
    time.sleep(2)
    s(className='Button', label='返回').tap()
    time.sleep(2)
    # 点击获赞
    s(label='获赞').click()
    time.sleep(2)
    my56 = s(className='Button', label='确认').click_exists(5)
    time.sleep(1)
    if my56:
        print('my56执行成功,当前状态 --%s' % my56)
    else:
        print('my56执行失败,当前状态 --%s' % my56)
    time.sleep(2)

    '''作品,赞过,收藏暂时不能点击,页面暂时不能用s.swipe实现滑动'''
    s(className='Cell').find_elements()[3].click()     # 赞过双瀑布ugc_list
    time.sleep(2)
    k = s(className='Button', name='bg btn tuf nor').find_elements()
    for i in range(len(k)):
        if k[i].value == '1':
            print('第%s个点赞状态为真' % i)
        else:
            print('第%s个点赞状态为假' % i)

    s(className='Cell').find_elements()[5].click()      # 第二个ugc详情页
    time.sleep(3)
    my57 = s(label='说点什么吧...').exists
    if my57:
        print('my57执行成功,当前状态 --%s' % my57)
    else:
        print('my57执行失败,当前状态 --%s' % my57)
    time.sleep(2)

    s(className='Button', name='返回').click()
    print('57条用例执行完毕,当前停留在我的主页')


