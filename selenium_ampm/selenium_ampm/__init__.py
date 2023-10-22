#= ライブラリ =#
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from itertools import combinations

#= 自作モジュール =#
from selenium_ampm.selenium_operations import SeleniumOperations
from selenium_ampm.html_tag_diff import *
from selenium_ampm.selenium import *

def main(urls):
  # seleniumでhtmlを取得する
  htmls = []
  for html in run_selenium('get_htmls', 'return', urls):
    tag_of_html = remove_content(html)
    formatted_tag_of_html = format_html(tag_of_html)
    htmls.append((url, formatted_tag_of_html))
  for conpare_html_pair in combinations(htmls, 2):
    diff = get_diff(conpare_html_pair[0], conpare_html_pair[1])

# 動作確認の簡易テスト
if __name__ == '__main__':
  None
