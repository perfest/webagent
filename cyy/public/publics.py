import time

def fs(s):
    s(label='粉丝').click()
    time.sleep(2)
    s(label='返回').click()
    time.sleep(2)
    s(label='粉丝').click()
    time.sleep(2)
    s(label='农夫').click()
    time.sleep(2)
    s(label='nav ico back').click()
    time.sleep(2)
    s(label='农夫').click()
    time.sleep(2)
    s(label='nav share').click()
    time.sleep(2)
    s(label='nav cross').click()
    time.sleep(1)
    s(label='nav ico back').click()
    time.sleep(2)
    s(label='互关注').click()
    time.sleep(2)
    s(label='取消').click()
    time.sleep(2)
    s(label='互关注').click()
    time.sleep(2)
    s(label='确定').click()
    time.sleep(2)
    s(label='关注').click()
    time.sleep(2)
    s(label='nav ico back').click()
    time.sleep(2)
