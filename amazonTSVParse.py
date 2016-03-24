#!/usr/bin/env python
# coding=utf-8

import sys
import csv

def change_date(target_date):
    # 日付表記を変換
    date_list = target_date.split()
    month = date_list[0]
    day = date_list[1]
    year=date_list[2]

    # 月名を変換
    if month=="January":
        month="1"
    elif month=="February":
        month="2"
    elif month=="March":
        month="3"
    elif month=="April":
        month="4"
    elif month=="May":
        month="5"
    elif month=="June":
        month="6"
    elif month=="July":
        month="7"
    elif month=="August":
        month="8"
    elif month=="September":
        month="9"
    elif month=="October":
        month="10"
    elif month=="November":
        month="11"
    elif month=="December":
        month="12"
    else:
        month="999"

    # 日部分を変換
    day=day[:-1]

    return "-".join([year,month,day])

line_count=0

if __name__ == "__main__":
    file_name=sys.argv[1]

with open(file_name,'r') as f:
    for line in f:
        itemList = line[:-1].split('\t')
        if line_count>2:
            itemList[5] = change_date(itemList[5])
        # リストから元に戻して出力する
        if line_count>1:
            print "\t".join(itemList)
        line_count += 1
