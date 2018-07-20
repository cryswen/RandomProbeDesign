

from selenium import webdriver
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup



NAconc = '500'
MGconc = '330'
temp = 30

candidate_file = pd.read_csv('../output_11word/blast_results_40.csv')

ids = candidate_file['id']
seqs = candidate_file['sequence']

url = 'https://www.idtdna.com/calc/analyzer'
driver = webdriver.Chrome()


def idtAnalyzer(seq):
    driver.get(url)
    SEQ_XPATH = '//textarea[@rows="5"]'
    seq_box = driver.find_element_by_xpath(SEQ_XPATH)
    seq_box.clear()
    seq_box.send_keys(seq)
    for option in driver.find_elements_by_tag_name('option'):
        if option.text == 'RNA':
            option.click()
            break
    NA_XPATH = '//input[@data-bind="value: naConc"]'
    NAconc_box = driver.find_element_by_xpath(NA_XPATH)
    NAconc_box.clear()
    NAconc_box.send_keys(NAconc)
    MG_XPATH = '//input[@data-bind="value: mgConc"]'
    MGconc_box = driver.find_element_by_xpath(MG_XPATH)
    MGconc_box.clear()
    MGconc_box.send_keys(MGconc)
    analyze_button = driver.find_element_by_id('analyze-button')
    analyze_button.click()
    time.sleep(5)
    T_XPATH = '//span[@data-bind="text: meltTemp() + \' ºC\'"]'
    new_value = driver.find_element_by_xpath(T_XPATH)
    return new_value.text


temps = []

for i in range(len(candidate_file)):
    id_num = ids[i]
    seq = seqs[i]
    temp = idtAnalyzer(seq)
    temps.append(temp)
    print(str(i+1) + ': ' + id_num + ' melting temperature is ' + temp + '.')
    


df = pd.concat([candidate_file,pd.Series(temps).rename('temp')],axis=1)
df.to_csv('../idt_out/idt_out.csv')

