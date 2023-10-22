from bs4 import BeautifulSoup, NavigableString
import difflib

#= 自作モジュール =#
from selenium_ampm.util import *

# htmlを整形する処理
def format_html(html_code):
  soup           = BeautifulSoup(html_code, 'html.parser')
  formatted_html = soup.prettify()
  return formatted_html

# htmlからタグ以外の要素を削除する処理
def remove_content(node):
  if isinstance(node, NavigableString):
    node.replace_with('')
  else:
    for child in node.children:
      remove_content(child)

# htmlの差分を取得する処理
def get_diff(text1, text2):
  d = difflib.Differ()
  diff = d.compare(text1.splitlines(), text2.splitlines())
  with open(f"{url_to_filename(text1)}_{url_to_filename(text2)}_diff.html", 'w', encoding='utf-8') as f:
    f.write('\n'.join(diff))


#= ファイルに書き込む感じの処理 =#
def save_only_tag(urls):
  for url in urls:
    html = f"{url_to_filename(url)}.html"
    with open(html, 'r', encoding='utf-8') as f:
      html = f.read()
      soup = BeautifulSoup(html, 'html.parser')
      remove_content(soup)
      with open(f"{url_to_filename(url)}_only_tag.html", 'w', encoding='utf-8') as f:
        f.write(str(soup))

def get_diff_by_saved(url1, url2):
  html1 = f"{url_to_filename(url1)}_only_tag.html"
  with open(html1, 'r', encoding='utf-8') as f:
    text1 = format_html(f.read())
  html2 = f"{url_to_filename(url2)}_only_tag.html"
  with open(html2, 'r', encoding='utf-8') as f:
    text2 = format_html(f.read())
  d = difflib.Differ()
  diff = d.compare(text1.splitlines(), text2.splitlines())
  with open(f"{url_to_filename(url1)}_{url_to_filename(url2)}_diff.html", 'w', encoding='utf-8') as f:
    f.write('\n'.join(diff))

if __name__ == '__main__':
  # urls = [
  #   'https://www.bing.com'
  #   , 'https://www.bing.com_2'
  # ]
  # get_only_tag(urls)
  get_diff('https://www.bing.com', 'https://www.bing.com_2')
