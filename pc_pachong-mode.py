import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)

def main():
    gevent.joinall([
            gevent.spawn(downloader, "1.jpg", "https://img.alicdn.com/imgextra/i3/30557696/O1CN01W0QoE526iotrdQMqk_!!0-saturn_solar.jpg_468x468q75.jpg"),
            gevent.spawn(downloader, "2.jpg", "https://img.alicdn.com/imgextra/i3/125362664/O1CN01TRAVVb1VY9uDgVKDr_!!0-saturn_solar.jpg_468x468q75.jpg")
    ])

if __name__ == "__main":
    main()