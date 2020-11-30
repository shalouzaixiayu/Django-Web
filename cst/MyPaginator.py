# -*- coding :  utf-8 -*-
# @Time      :  2020/11/19  15:51
# @author    :  沙漏在下雨
# @Software  :  PyCharm
# @CSDN      :  https://me.csdn.net/qq_45906219

from django.core.paginator import Paginator


class MyPaginator(Paginator):
    def __init__(self, now_page, max_display_page, object_list, per_page, orphans=0, allow_empty_first_page=True):
        """
             对这个类进行重写
             :param now_page:  当前页数
             :param max_display_page:   最大展示页数,  如果数据量很大， 我们只能让他动态的展示最大页数
        """
        super().__init__(object_list, per_page, orphans, allow_empty_first_page)
        self.now_page = int(now_page)
        self.max_display_page = int(max_display_page)

    @property
    def page_range(self):
        """
        重写这个页码范围显示办法
        :return:   返回自定义的页码范围
        """

        # 如果总页数 < 最大页数   eg: 最大页数没有达到 最大展示页数  max_display_page
        if self.num_pages < self.max_display_page:
            return range(1, self.num_pages + 1)

        # 如果总页数 > 最大页数
        # 数据特别多的时候
        half_page = int(self.max_display_page // 2)
        if self.now_page <= half_page:
            return range(1, self.max_display_page + 1)
        if (self.now_page + half_page) > self.num_pages:
            return range(self.num_pages - self.max_display_page + 1, self.num_pages + 1)
        return range(self.now_page - half_page + 1, self.now_page + half_page + 1)
