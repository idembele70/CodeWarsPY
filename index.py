import re
def remove_url_anchor(url):
  return re.sub('#.*', '', url)

print(remove_url_anchor("www.codewars.com#about"))