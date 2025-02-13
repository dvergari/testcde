import urllib.request
import sys
import ssl


def download(url, filename):
    try:
        ssl._create_default_https_context = ssl._create_unverified_context
        urllib.request.urlretrieve(url, filename)
        print("Downloaded: {}".format(filename))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: download.py <url> <filename>")
        sys.exit(1)

    url = sys.argv[1]
    filename = sys.argv[2]

    download(url, filename)







