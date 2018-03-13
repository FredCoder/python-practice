# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from LotterySpider.items import LotteryspiderItem
import re


class SsqSpider(scrapy.Spider):
    name = 'ssq'
    allowed_domains = ['kaijiang.zhcw.com']
    start_urls = ['http://kaijiang.zhcw.com/zhcw/inc/ssq/ssq_wqhg.jsp?pageNum=1']

    # 最后一页flag
    LAST_PAGE_FLAG = False

    def parse(self, response):
        row_nodes = response.css("table tr")
        for row in row_nodes:
            cells = row.css("td")
            if len(cells) != 0 and re.match("(\d{4})-(\d{2})-(\d{2})", cells[0].css("::text").extract()[0].strip()):
                item = LotteryspiderItem()
                try:
                    date = cells[0].css("::text").extract()[0]
                    item["date"] = date  # 日期
                    item["issue"] = cells[1].css("::text").extract()[0]  # 期号
                    item["number1"] = cells[2].css("em::text").extract()[0]  # 号码1
                    item["number2"] = cells[2].css("em::text").extract()[1] # 号码2
                    item["number3"] = cells[2].css("em::text").extract()[2]  # 号码3
                    item["number4"] = cells[2].css("em::text").extract()[3]  # 号码4
                    item["number5"] = cells[2].css("em::text").extract()[4]  # 号码5
                    item["number6"] = cells[2].css("em::text").extract()[5]  # 号码6
                    item["numberEx"] = cells[2].css("em::text").extract()[6]  # 号码7
                    item["sales"] = cells[3].css("::text").extract()[0]  # 销售额（元）
                    item["first_prize"] = cells[4].css("::text").extract()[0]  # 一等奖注数
                    item["second_prize"] = cells[5].css("::text").extract()[0]  # 二等奖注数
                    item["place"] = cells[4].css("::text").extract()[1].strip()  # 地点
                except Exception as e:
                    print(e)
                yield item

        # 读取下一页的标签
        last_row = row_nodes.css("tr:last-child")
        next_page_url = last_row.css("a::attr(href)")[2].extract()
        last_page_url = last_row.css("a::attr(href)")[3].extract()

        if next_page_url != last_page_url or not self.LAST_PAGE_FLAG:
            yield Request(url=parse.urljoin(response.url, next_page_url), callback=self.parse)
        if next_page_url == last_page_url:
            self.LAST_PAGE_FLAG = True


