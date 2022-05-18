#encoding:utf-8
import datetime

day1 = day3 = day7 = day30 = other = 0

def change_day():
    global day1
    global day3
    global day7
    global day30
    global other
    day1 = day3 = day7 = day30 = other = 0

def create_time(timestamp):
    if timestamp<60*60*24:
        global day1
        day1+=1
    if timestamp<60*60*24*3:
        global day3
        day3 += 1
    if timestamp < 60 * 60 * 24 * 7:
        global day7
        day7 += 1
    if timestamp < 60 * 60 * 24 * 30:
        global day30
        day30 += 1
    if timestamp>0:
        global other
        other += 1

def create_post_bar():
    from pyecharts import Bar
    bar = Bar("文章分析", "文章发布量分析")
    bar.add("文章", ["今天", "3天内文章", "7天内文章", "30内文章","总共文章"], [day1,day3,day7,day30,other],is_more_utils=True)
    return bar

def create_pie_bar():
    from pyecharts import Pie
    pie = Pie("评论分析")
    pie.add("",["今天", "3天内评论", "7天内评论", "30内评论","总共评论"], [day1,day3,day7,day30,other],is_more_utils=True)
    return pie



