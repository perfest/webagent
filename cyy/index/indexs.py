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

