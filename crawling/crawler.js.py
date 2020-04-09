import os
import sys

import requests_html
import urllib3
from urllib3.contrib import pyopenssl
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import pyppdf.patch_pyppeteer
pyopenssl.extract_from_urllib3()


def readUrls(file_name = 'Alexa_topsites.txt'):
    file = open(file_name, 'r')
    urls = file.read().splitlines()
    file.close()
    return ['http://www.' + url for url in urls]


if __name__ == '__main__':
    file_name = sys.argv[1] if len(sys.argv) > 1 else 'Alexa_topsites.txt'
    folder_name = sys.argv[2] if len(sys.argv) > 2 else 'benign'
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    urls = readUrls(file_name)
    total = len(urls)
    current = 0
    for url in urls:
        current += 1
        session = requests_html.HTMLSession(verify=False)
        try:
            print('Crawling %s (%d / %d)' % (url, current, total))
            r = session.get(url, verify=False)
            r.html.render(retries=4, sleep=1, wait=1)
            scripts = r.html.find('script')
            r.close()
        except:
            session.close()
            continue
        i = 1
        for script in scripts:
            if 'type' in script.attrs and script.attrs['type'] == 'text/javascript' and 'src' not in script.attrs:
                name = '%s/%s/%s-%d.js' % (os.getcwd(), folder_name, url[7:], i)
                file = open(name, 'w')
                file.write(script.text)
                file.flush()
                file.close()
                i += 1

        session.close()
