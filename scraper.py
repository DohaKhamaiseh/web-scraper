import requests
from bs4 import BeautifulSoup
import json

URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'

page = requests.get(URL)
# print(page)
# print(page.content)

# conver from byte tp html
soup = BeautifulSoup(page.content, 'html.parser')


posts_list = []


def get_citations_needed_count():
     """
     this function will count how many times the citation needed appear
     """
     count = 0
  
     comments_tag = soup.find_all('sup', class_='noprint Inline-Template Template-Fact')
     for co in comments_tag:
      if co:
       count+=1
     return count




print(get_citations_needed_count())

def get_citations_needed_report():
  """
  this function will return the paragraph that needs a citation
  """
  all_para = soup.find_all('p')
  report = ""
  p = []
  rm = ""
  for para in all_para:
    comments_tag = para.find('sup', class_='noprint Inline-Template Template-Fact')
    if comments_tag:
       rm = para.text.replace("[citation needed]"," ")
       p.append(rm)
       report +='\n'.join(p)

  return report

print(get_citations_needed_report())
