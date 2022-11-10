import urllib.request

def main():
    req = urllib.request.urlopen("https://img.alicdn.com/imgextra/i3/30301515/O1CN01ce5G791N3uaiW52KX_!!0-saturn_solar.jpg_468x468q75.jpg")

    img_content = req.read()

    with open("1.jpg", "wb") as f:
        f.write(img_content)

if __name__ == "__main":
    main()