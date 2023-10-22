#= 自作モジュール =#
from selenium_ampm.util import *

class SeleniumOperations:
  """
  Selenium操作を行うための様々な関数を含むクラスです
  """

  def get_htmls(driver, mode: str, urls: list):
    """
    SeleniumのドライバーとURLのリストが与えられた場合、この関数は各URLに移動し、HTMLソースコードを'saved_html'ディレクトリ内のファイルに保存します。
    ファイル名は、文字または数字でない文字を削除してURLから生成されます。

    :param driver: Seleniumのドライバーオブジェクト
    :param mode: この関数の動作モード。return or save
    :param urls: HTMLソースコードを取得するために移動するURLのリスト
    """
    for url in urls:
      driver.get(url)
      html = driver.page_source
      if mode == 'return':
        yield html
      elif mode == 'save':
        with open(f"./saved_html/{url_to_filename(url)}.html", 'w', encoding='utf-8') as f:
          f.write(html)
      else:
        raise ValueError('modeにはreturnかsaveを指定してください。')
