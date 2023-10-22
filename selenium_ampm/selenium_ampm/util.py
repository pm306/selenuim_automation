#= ライブラリ =#
import re

def url_to_filename(url):
  './saved_html/' + re.sub('[./:]', '', url)
