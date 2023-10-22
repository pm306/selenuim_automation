#= ライブラリ =#
from selenium import webdriver
from selenium.webdriver.edge.service import Service

#= 自作モジュール =#
from selenium_ampm.selenium_operations import SeleniumOperations

def run_selenium(mode, *args):
  # 安定版Edgeのドライバーを起動
  service = Service('./../assets/msedgedriver.exe')
  driver  = webdriver.Edge(service=service)

  # 具体的な動作はSeleniumOperationsクラスに定義
  getattr(SeleniumOperations, mode)(driver, *args)

  # ドライバーを閉じる
  driver.quit()

# 動作確認の簡易テスト
if __name__ == '__main__':
  urls = [
    'https://www.google.com',
    'https://www.yahoo.co.jp',
    'https://www.bing.com'
  ]
  run_selenium('get_htmls', urls)
