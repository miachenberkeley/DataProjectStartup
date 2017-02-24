from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import xlsxwriter
import csv
import re
import time
"""
workbook = xlsxwriter.Workbook('company.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 0, "fonds")
worksheet.write(0, 1, "founder name")
worksheet.write(0, 2, "startups")
path = '/Users/chen/Desktop/DataProject/investors-2-2-2017.csv' """


def get_data_crunchbase(driver,url):
    start = time.time()
    driver.get(url)
    infos = {}
    list_entreprise = []
    list_investissement = []
    try:
        infos['founder_name'] = driver.find_element_by_class_name('follow_card').text
        infos['entreprises'] = driver.find_element_by_css_selector(
        'table.section-list.table.investors').find_elements_by_css_selector('a.follow_card')

        infos["investissement"] = driver.find_element_by_css_selector(
        'table.section-list.table.investors').find_elements_by_css_selector('td')

        for entreprise in infos['entreprises']:
            try:
                list_entreprise.append(entreprise.text)
            except NoSuchElementException:
                print("profile non trouve")
                list_entreprise.append("None")
        infos['entreprises'] = list_entreprise

       # for investissement in infos['investissement']:
        #    try:
         #       list_investissement.append(investissement.text)
          #  except NoSuchElementException:
           #     print("profile non trouve")
            #    list_entreprise.append("None")
        #infos['investissement'] = list_investissement


    except NoSuchElementException:
        print("entreprise non trouve")
    print('It took ' + str((time.time() - start) / 1000) + ' seconds!')
    return infos

driver = webdriver.Firefox()
print(get_data_crunchbase(driver,'https://www.crunchbase.com/organization/sequoia-capital'))

'''
nb_of_file = 0

with open(path, 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')


    for i in enumerate(spamreader):
        if i ==0:
            pass
        else:
            worksheet.write(nb_of_file, 0, spamreader[i][0])
            #print(spamreader[i][1])
            driver = webdriver.Firefox()
            list = get_data_crunchbase(driver, spamreader[i][1])
            worksheet.write(nb_of_file, 1, list['founder_name'])
            worksheet.write(nb_of_file, 2, ', '.join(list['entreprises']))
            nb_of_file += 1
'''










