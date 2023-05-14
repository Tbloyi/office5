import time
import os

# 设置专注时间（单位：秒）
focus_time = 25 * 60

# 倒计时函数
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end='\r')
        time.sleep(1)
        t -= 1

    # 播放提示音
    os.system('afplay /System/Library/Sounds/Ping.aiff')

# 开始倒计时
countdown(focus_time)

print('时间到！')
