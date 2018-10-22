# -*- coding: utf-8 -*-
import scrapy
from weather.items import WeatherItem


class TianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['tianqi.com']
    start_urls = ['http://hailaer.tianqi.com']

    def parse(self, response):
        items=[]
        sevendays = response.xpath('//div[@class="day7"]')
        week_list = sevendays.xpath('./ul[@class="week"]/li')
        for day in week_list:
            item = WeatherItem()
            print(day)
            date = day.xpath('./b/text()').extract()[0]
            #print(date)
            day_of_the_week =day.xpath('./span/text()').extract()[0]
            #print(day_of_the_week)
            img = day.xpath('./img/@src').extract()[0]
            item['date'] = date
            item['week'] = day_of_the_week
            item['img'] = img
            print("img:",img)
            items.append(item)
        
        weather_list = sevendays.xpath('./ul[@class="txt txt2"]/li')
        for index,weather in enumerate(weather_list):
            dayWeather = weather.xpath('./text()').extract()[0]
            print(dayWeather)
            items[index]['weather']=dayWeather
        
        temp_list = sevendays.xpath('./div[@class="zxt_shuju"]/ul/li')
        #  temp for temperature
        # print(temp_list)
        for index,temp in enumerate(temp_list):
            # print(temp)
            low_temp = temp.xpath('./b/text()').extract()[0]
            high_temp = temp.xpath('./span/text()').extract()[0]
            print(low_temp)
            print(high_temp)
            items[index]['temperature']=str(low_temp)+"~"+str(high_temp)
       

        wind_list = sevendays.xpath('./ul[@class="txt"]/li')
        for index,wind in enumerate(wind_list):
            dayWind = wind.xpath('./text()').extract()[0]
            print(dayWind)
            items[index]['wind'] = dayWind


        return items




        


        




