# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import csv
import pandas as pd
import numpy as np
import time
import os
class FoodmateScrapyPipeline(object):
    """ 
        功能：保存item数据 
    """
    
    def __init__(self):
        logging.info("FoodmateScrapyPipeline init...")
        self.jy_file = open('jjy.csv','a+',encoding='utf-8',newline='')
        self.header = ["信息来源","网站","搜索条件","产品/Product","产品分类/Product Category","规格型号","生产日期/通报编号/Reference","生产企业/Subject","不合格项（标准值）/Substance/Hazard","标准值","检验结果/Analytical Result","单位/Unit","发布单位/Notification from","发布日期/Date of case"]

        

    def process_item(self, item, spider):
        logging.info("FoodmateScrapyPipeline process_item...")
        csv_writer = csv.writer(self.jy_file)
        row = []
        for col in self.header:
            if col in item:
                row.append(item[col])
            else:
                row.append("")
        csv_writer.writerow(row)
        return item

    def close_spider(self, spider):
        logging.info("FoodmateScrapyPipeline close...")
        self.jy_file.close
        # time.sleep(5)
        # csvf = pd.read_csv('调味品.csv', encoding='utf-8')
        # if os.path.isfile('调味品.xlsx') == True:
        #     os.remove('调味品.xlsx')
        # time.sleep(1)
        # csvf.to_excel('调味品.xlsx', sheet_name='data')