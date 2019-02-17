

'''
固定点击特定的元素,校验埋点是否有上报
首页上的视频,点击播放,通过label拿到他的text  保存为变量
拿到当前点击的时间   time.time()   保存变量
固定当前元素 上报的埋点名字  保存变量
拿到固定的手机设备号




埋点文件
根据手机的设备号  查询埋点    校验埋点字段是否存在   存在有上报   校验时间  校验时间给定一个返回  只要记录的时间在上报的这个时间范围内就可以
没有说明上报有问题
c.status # 获取当前设备信息
{'state': 'success',
'os': {'name': 'iOS', 'version': '12.1'},
'ios': {'simulatorVersion': '12.1', 'ip': '192.168.2.139'},
'build': {'time': 'Feb 12 2019 17:21:54'},
'sessionId': '3544EEA7-6C90-44A4-8DBD-1BCDAE051D01'}


'''


def point(c,s):
    # 打开设备   记录当前时间   查看是否有上报 app_start
    c.session('com.dealuck.cyyapp')
    import time
    m = time.time()     # 获取当前的时间  校验时间时 埋点时间必须>=当前时间
    l = c.staus()   # 获取设备的信息
    '''
    {'state': 'success',
    'os': {'name': 'iOS', 'version': '12.1'},
    'ios': {'simulatorVersion': '12.1', 'ip': '192.168.2.139'},
    'build': {'time': 'Feb 12 2019 17:21:54'},
    'sessionId': '3544EEA7-6C90-44A4-8DBD-1BCDAE051D01'}
    '''
    # 调用 埋点校验函数(m,l,'可以写死用户id','埋点table_name')



    # 来到首页滑动事件   记录当前时间   查看是否有上报 homepage_page_loaded
    s.swipe(100, 700, 100, 300)

    # 离开首页时   记录时间  查看是否有上报  homepage_tab_click 和 homepage_stay
    s(label='我的').click()

