# -*- coding :  utf-8 -*-
# @Time      :  2020/11/24  16:11
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219
import time
import turtle as t


class GetInitialDate(object):
    #  The first date
    #  请更换你的纪念日， 如果数量很多， 可以生成列表，
    #  遍历传值，不懂的可以私聊我
    #  其实这个天数也可以直接从对象中传值过来，但是必须得是 ****-**-** 这样的格式
    Initial_date = "2018-08-17"

    def __init__(self):
        self.date_item = self.get_items
        self.now_date = self._get_now_date()
        # self.Initial_date_sum = self.get_sum_date(self.Initial_date)
        # self.now_date_sum = self.get_sum_date(self.now_date)
        self.all_date = self.get_sum_date(self.Initial_date, self.now_date)

    def __str__(self):
        """稍微修饰一下,"""
        return f"我来啦".center(40,
                             '-') + f"\n不错哟, 你们已经认识这么长时间了, 足足有 {self.all_date} 天呢\n希望你们在接下里的时间, 能够更加细腻的陪伴,感谢有你!\n" + "我一直在!".center(
            40, '-')

    @property
    def get_items(self):
        """遍历或者字典天数
         as:  {1: 31, 2: 59, 3: 90, 4: 120, 5: 151, 6: 181, 7: 212, 8: 243, 9: 273, 10: 304, 11: 334, 12: 365}
         如果是闰年 后续需要加一天"""
        date_items = {}
        s = 0
        for i in range(1, 13):
            if i in [1, 3, 5, 7, 8, 10, 12]:
                s += 31
            elif i == 2:
                s += 28
            else:
                s += 30
            date_items[i] = s
        return date_items

    def get_sum_date(self, old_date, new_date):
        """ start sum the date """
        old_year, old_month, old_d = map(int, old_date.split("-"))
        new_year, new_month, new_d = map(int, new_date.split('-'))
        #  先计算初始日期的天数
        is_leap = True if self._is_leap(old_year) else False
        if not is_leap:
            The_date = self.date_item[old_month] + old_d
        else:
            The_date = self.date_item[old_month] + 1 + old_d
            # 计算新的日期
        is_leap_now = True if self._is_leap(new_year) else False
        if not is_leap:
            The_date_now = self.date_item[new_month] + new_d
        else:
            The_date_now = self.date_item[new_month] + 1 + new_d
        # 比较

        if old_year == new_year:
            return The_date_now - The_date + 2
        else:
            # 2019  2020
            ss = 0
            for i in range(new_year - old_year):
                if self._is_leap(old_year + i):
                    s = 366
                else:
                    s = 365
                ss += s
            return ss + The_date_now - The_date + 2

    def _get_now_date(self):
        """Return the  localtime as: "****-**-**" date """
        return time.strftime("%Y-%m-%d", time.localtime())

    def _is_leap(self, year):
        "year -> 1 if leap year, else 0."
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


class Rose:
    mystr = GetInitialDate()

    def __init__(self):
        one, two, three, four = str(self.mystr).split("\n")
        self.str_item = {1: one, 2: two, 3: three, 4: four}
        self.start()
        pass

    def ggg(self, n, r, d=1):  # 曲线绘制
        for i in range(n):
            t.left(d)
            t.circle(r, abs(d))

    def start(self):
        """draw the rose """
        s = 0.2  # size
        t.setup(450 * 5 * s, 750 * 5 * s)
        t.pencolor("black")
        t.fillcolor("red")
        t.speed(-1)
        t.penup()
        t.goto(0, 900 * s)
        t.pendown()
        # 绘制花朵形状
        t.begin_fill()
        t.circle(200 * s, 30)
        self.ggg(60, 50 * s)
        t.circle(200 * s, 30)
        self.ggg(4, 100 * s)
        t.circle(200 * s, 50)
        self.ggg(50, 50 * s)
        t.circle(350 * s, 65)
        self.ggg(40, 70 * s)
        t.circle(150 * s, 50)
        self.ggg(20, 50 * s, -1)
        t.circle(400 * s, 60)
        self.ggg(18, 50 * s)
        t.fd(250 * s)
        t.right(150)
        t.circle(-500 * s, 12)
        t.left(140)
        t.circle(500 * s, 110)
        t.left(27)
        t.circle(650 * s, 100)
        t.left(130)
        t.circle(-300 * s, 20)
        t.right(123)
        t.circle(220 * s, 57)
        t.end_fill()
        # 绘制花枝
        t.left(120)
        t.fd(280 * s)
        t.left(115)
        t.circle(300 * s, 33)
        t.left(180)
        t.circle(-300 * s, 33)
        self.ggg(70, 225 * s, -1)
        t.circle(350 * s, 104)
        t.left(90)
        t.circle(200 * s, 105)
        t.circle(-500 * s, 63)
        t.penup()
        t.goto(150 * s, -10 * s)
        t.pendown()
        t.left(160)
        self.ggg(20, 2400 * s)
        self.ggg(220, 250 * s, -1)
        # 绘制一个绿色叶子
        t.fillcolor("green")
        t.penup()
        t.goto(670 * s, -180 * s)
        t.pendown()
        t.right(140)
        t.begin_fill()
        t.circle(300 * s, 120)
        t.left(60)
        t.circle(300 * s, 120)
        t.end_fill()
        t.penup()
        t.goto(180 * s, -550 * s)
        t.pendown()
        t.right(85)
        t.circle(600 * s, 40)
        # 绘制第二个绿色叶子
        t.penup()
        t.goto(-150 * s, -1000 * s)
        t.pendown()
        t.begin_fill()
        t.right(120)
        t.circle(300 * s, 115)
        t.left(75)
        t.circle(300 * s, 100)
        t.end_fill()
        t.penup()
        t.goto(430 * s, -1070 * s)
        t.pendown()
        t.right(30)
        t.circle(-600 * s, 35)
        # 文字部分
        t.pensize(4)
        t.pencolor("purple")
        t.penup()
        t.goto(-800 * s, -200 * s)
        t.pendown()
        t.write("我们不需要过多解释", align="left", font=("arial", 10, "normal"))
        t.penup()
        t.goto(-800 * s, -300 * s)
        t.pendown()
        t.write("只需要一如既往", align="left", font=("arial", 10, "normal"))
        t.penup()
        t.goto(-750 * s, -400 * s)
        t.pendown()
        t.write("奔跑，奔跑，继续奔跑！！", align="left", font=("arial", 10, "normal"))
        for i in range(1, 5):
            t.penup()
            t.goto(-750 * s, 1500 * s)
            if i == 1:
                pass
            else:
                t.goto(-750 * s, (1500 - 100 * i) * s)
            t.pendown()
            t.write(f"{self.str_item[i]}", align="left", font=("arial", 10, "normal"))
        t.hideturtle()
        t.done()


# a = Rose()
print(GetInitialDate())
