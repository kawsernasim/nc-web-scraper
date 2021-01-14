# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from db_helper import *

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

        del self.db.add_paper(id, board, qualification, subject, year, session, paper_type, link)


    def close_spider(self, spider):
        pass
        
        

