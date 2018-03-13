# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb


class LotteryspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(
            '192.168.70.45',
            'root',
            '123456',
            'lottery_spider',
            charset='utf8',
            use_unicode=True
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into ssq(id, date, issue, number1, number2, number3, number4, number5, number6, numberEx, sales,
             first_prize, second_prize, place) 
            VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (
        item["date"], item["issue"],
        item["number1"],
        item["number2"],
        item["number3"],
        item["number4"],
        item["number5"],
        item["number6"],
        item["numberEx"],
        item["sales"],
        item["first_prize"],
        item["second_prize"],
        item["place"]))
        self.conn.commit()
