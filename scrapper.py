import requests
import json

class ScrapperShopee:
    url = None
    price = None
    line = 0

    
    def __init__(self, url, line):
        urllist = url.split(".")
        if(len(urllist) == 5):
            if(urllist[0].find('shopee') == -1):
                raise Exception(("Link pada baris ke-{} tidak valid ! ! !").format(line))
            else:
                self.line = 0
                self.line = line
                itemid = urllist[-1]
                shopid = urllist[-2]
                self.url = "https://shopee.co.id/api/v2/item/get?itemid="+itemid+"&shopid="+shopid
        else:
            raise Exception("Link pada baris ke-"+self.line+" tidak valid ! ! !")


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
            raise Exception(("Produk pada baris ke-{} tidak tersedia ! ! !").format(self.line))
