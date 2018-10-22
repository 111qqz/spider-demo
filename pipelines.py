# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import os
import requests
import json


class WeatherPipeline(object):
    def process_item(self, item, spider):
        print("miao miao miao pipeline*******8")
        base_dir = os.getcwd()
        filename = base_dir + '/data/result.txt'
        with open(filename, 'a') as f:
            f.write(item['date'] + '\n')
            f.write(item['week'] + '\n')
            f.write(item['temperature'] + '\n')
            f.write(item['weather'] + '\n')
            f.write(item['wind'] + '\n\n')


        return item

