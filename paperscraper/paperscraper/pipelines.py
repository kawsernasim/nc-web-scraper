# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from db_helper import *
from random import randint





class PaperscraperPipeline:
    def __init__(self):
        self.title = None
        self.link = None
        self.db = DBHelper()

    def open_spider(self, spider):
        pass
            
    def process_item(self, item, spider):
        content = item

        self.title = item['title']
        self.link = item['link']

        #split title into specific db columns (year, session, subject etc)

        id = randint(0, 1000)
        board = "Edexcel"
        qualification = "IGCSE"
        subject = "Mathematics B"
        title_grab = self.title[0]
        title_split = title_grab.split(' ')
        year = title_split[1]
        session = title_split[0]
        paper_type = 1
        a = self.link
        for i in a:
            link = i
        
        return self.db.add_paper(id, board, qualification, subject, year, session, paper_type, link)


    def close_spider(self, spider):
        pass
        
    