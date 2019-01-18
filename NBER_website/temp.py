import requests
import pandas as pd

path = '/home/kyle/Downloads/Public-A.html'
with open(path) as f:
    html = f.read()

url = 'https://www.nber.org/medicare/public/Public-A.html#toc-Appendix-A'
r = requests.get(url)

dfs = pd.read_html(html)
len(dfs)

from tabulate import tabulate
print(tabulate(dfs[1], tablefmt='pipe', showindex=False))

dfs[1]
