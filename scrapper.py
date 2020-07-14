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
                self.url = ("https://shopee.co.id/api/v2/item/get?itemid={}&shopid={}").format(itemid,shopid)
        else:
            raise Exception(("Link pada baris ke-{} tidak valid ! ! !").format(line))


    def scrappe(self):
        try:
            s = requests.Session()
            page = s.get(self.url)
            jsontext = json.loads(page.text)
            

            # Variable produk
            nama_produk = jsontext['item']['name']
            rating = str(jsontext['item']['item_rating']['rating_star'])
            rating = rating[:2]
            review = str(jsontext['item']['item_rating']['rcount_with_context'])
            harga_min = str(jsontext['item']['price']) # Perlu diganti template literal, kalau mau outputnya number
            harga_max = str(jsontext['item']['price_max']) # Perlu diganti template literal, kalau mau outputnya number
            harga_min = harga_min[:-5]
            harga_max = harga_max[:-5]
            deskripsi = str(jsontext['item']['description'])
            stock = str(jsontext['item']['normal_stock'])
            pengiriman = str(jsontext['item']['shop_location'])
            link_gambar = []

            for i in jsontext['item']['images']:
                link_gambar.append(("https://cf.shopee.co.id/file/{}").format(i))
            
            print("==========================")
            print(("Nama Produk: {}").format(nama_produk))
            print(("Rating Produk: {} , dari {} review ").format(rating, review))

            if(harga_max == harga_min):
                print(("Harga Produk: Rp {}").format(harga_min))
            else:
                print(("Harga Produk: dari Rp {} sampai Rp {}").format(harga_min, harga_max))

            print(("Deskripsi: {}").format(deskripsi))

            print(("Sisa Stock: {}").format(stock))

            print(("Dikirim dari: {}").format(pengiriman))

            print(("Link Gambar : {}").format(link_gambar))            

                
            print("==========================")
        except:
            raise Exception(("Produk pada baris ke-{} tidak tersedia ! ! !").format(self.line))
