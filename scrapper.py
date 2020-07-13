import requests
import json

class ScrapperShopee:
    url = None
    price = None

    
    def __init__(self, url):
        urllist = url.split(".")
        itemid = urllist[-1]
        shopid = urllist[-2]
        self.url = "https://shopee.co.id/api/v2/item/get?itemid="+itemid+"&shopid="+shopid


    def getPrice(self):
        try:
            s = requests.Session()
            page = s.get(self.url)
            jsontext = json.loads(page.text)
            harga_min = str(jsontext['item']['price'])
            harga_max = str(jsontext['item']['price_max'])
            harga_min = harga_min[:-5]
            harga_max = harga_max[:-5]
            if(harga_max == harga_min):
                print("harga_produk: Rp "+harga_min)
            else:
                print("Harga produk berkisar dari Rp "+harga_min+" sampai Rp "+harga_max)
        except:
            print("Gagal")
