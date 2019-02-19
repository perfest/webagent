import  time


def indexs(c,s):
    # 点击首页
    s(label='首页').click()
    time.sleep(3)
    print("执行首页的测试用例")
    s.swipe(100, 700, 100, 300)         # 向上滑动事件
    s.swipe(100, 300, 100, 700)         # 向下滑动事件
    s.swipe(100, 300, 400, 300)         # 向右滑动事件
    s.swipe(400, 300, 100, 300)         # 向左滑动事件

    s.swipe_right()
    s.swipe_left()                      # 可以实现左右滑动事件

    print('首页滑动事件完成')
    s(className='Cell').find_elements()[3].tap()
    time.sleep(3)
    s(label='首页').click()
    time.sleep(3)
    txt = s(className='StaticText').find_elements()[5].text
    print('现在点击的是--------------{}'.format(txt))
    time.sleep(1)
    s(className='StaticText').find_elements()[5].tap()
    time.sleep(3)
    s(label='首页').click()        # 点击返回
    time.sleep(3)
    # s(className='StaticText').find_elements()[5].tap()      # 首页中无法实现点击用户昵称实现跳转
    s(label='bg btn tuf nor', className='Button').find_elements()[3].click()      # 实现小心心的点击
    time.sleep(2)
    l = range(4)
    for i in l:
        s(label='bg btn tuf nor', className='Button').find_elements()[i].click()
        print('第{}个小心心的点击事件'.format(i))
        time.sleep(1)

    s.swipe_left()
    time.sleep(2)
    s.swipe_left()
    time.sleep(2)
    s.swipe_left()
    time.sleep(2)
    s.swipe_left()
    time.sleep(2)
    s.swipe_left()
    time.sleep(2)       # 5次左滑事件完成以后  现在停留在'生活'tab下

    for i in l:
        s(label='bg btn tuf nor', className='Button').find_elements()[i].click()
        print('第{}个小心心的点击事件'.format(i))
        time.sleep(1)           # 在当前页面实现点赞

    s(className='StaticText').find_elements()[3].tap()        # 点击进入ugc详情页
    time.sleep(3)

    '''
    第--1--个Button的text是=======喜欢
    第--2--个Button的text是=======评论
    第--3--个Button的text是=======收藏
    第--4--个Button的text是=======关注
    第--5--个Button的text是=======分享
    第--6--个Button的text是=======rightbar btn more1
    第--7--个Button的text是=======东东-哈士奇
    第--8--个Button的text是=======宠物生活秀
    第--9--个Button的text是=======bg btn play
    第--10--个Button的text是=======amplification
    注意:1,2 如果有点赞或评论数量 则text显示为 数字  
    '''
    l = range(1, 10)
    for i in l:
        m = s(className='Button').find_elements()[i].text
        print('第--{}--个Button的text是======={}'.format(i, m))
        if i == 1:
            pass
        else:
            s(className='Button').find_elements()[0].tap()







'''
ls = 所存的为当前页面ClassName为Image 的元素
for i in ls:
    i.tap()    实现这个页面所有元素的点击  但是点击以后需要返回
    time.sleep(1)
    if s(className=format{})format Button or '推荐' or nav back :
    if s(className=format{}).exists : format Button or '推荐' or nav back 
    如果页面上存在这个元素 点击返回
    进行下一次的元素点击
'''


