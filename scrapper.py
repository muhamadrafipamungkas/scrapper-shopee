import requests
import json

class ScrapperShopee:
    url = None
    price = None
    line = 0
    
    def __init__(self, url, line):
        urllist = url.split(".")    # Convert link produk menjadi list (array) dengan nilai pemisah berupa "."
        if(len(urllist) == 5):
            if(urllist[0].find('shopee') == -1): # Memastikan link merupakan link shopee
                raise Exception(("Link pada baris ke-{} tidak valid ! ! !").format(line))
            else:
                self.line = 0
                self.line = line
                itemid = urllist[-1]
                shopid = urllist[-2]
                # Url API produk
                self.url = ("https://shopee.co.id/api/v2/item/get?itemid={}&shopid={}").format(itemid,shopid)
        else:
            raise Exception(("Link pada baris ke-{} tidak valid ! ! !").format(line))


    def scrappe_first(self):
        try:
            # Membuat request ke API Shopee
            s = requests.Session()
            page = s.get(self.url) # Ambil response API
            jsontext = json.loads(page.text)
            

            # Variable produk

            nama_produk = jsontext['item']['name']

            rating = '{:.1f}'.format(jsontext['item']['item_rating']['rating_star'])

            review = jsontext['item']['item_rating']['rcount_with_context']

            harga = int((jsontext['item']['price'])/100000)

            deskripsi = str(jsontext['item']['description'])

            stok = jsontext['item']['normal_stock']

            variasi = []
            if(len(jsontext['item']['models'])>0):
                for i in jsontext['item']['models']:
                    variasi.append(i['name'])
                variasi = ', '.join([str(elem) for elem in variasi]) 
                variasi = variasi
            else:
                variasi = None

            link_gambar = []
            if(len(jsontext['item']['images'])>0):
                for i in jsontext['item']['images']:
                    link_gambar.append(("https://cf.shopee.co.id/file/{}").format(i))
                link_gambar = '\n'.join([str(elem) for elem in link_gambar])

            return [nama_produk, None,harga,None,stok,
                    variasi,rating,review,deskripsi,link_gambar]
                
        except:
            raise Exception(("Produk pada baris ke-{} tidak tersedia ! ! !").format(self.line))

    def scrappe_next(self,df,line):
        line -= 1
        try:
            # Membuat request ke API Shopee
            s = requests.Session()
            page = s.get(self.url) # Ambil response API
            jsontext = json.loads(page.text)
            

            # Variable produk

            nama_produk = jsontext['item']['name']

            rating = '{:.1f}'.format(jsontext['item']['item_rating']['rating_star'])

            review = jsontext['item']['item_rating']['rcount_with_context']

            harga_lama = df["Harga"][line]

            harga = int((jsontext['item']['price'])/100000)

            deskripsi = str(jsontext['item']['description'])

            stok_lama = df["Stok"][line]

            stok = jsontext['item']['normal_stock']

            variasi = []
            if(len(jsontext['item']['models'])>0):
                for i in jsontext['item']['models']:
                    variasi.append(i['name'])
                variasi = ', '.join([str(elem) for elem in variasi]) 
                variasi = variasi
            else:
                variasi = None

            link_gambar = []
            if(len(jsontext['item']['images'])>0):
                for i in jsontext['item']['images']:
                    link_gambar.append(("https://cf.shopee.co.id/file/{}").format(i))
                link_gambar = '\n'.join([str(elem) for elem in link_gambar])

            return [nama_produk, harga_lama,harga,stok_lama,stok,
                    variasi,rating,review,deskripsi,link_gambar]
                
        except:
            raise Exception(("Produk pada baris ke-{} tidak tersedia ! ! !").format(self.line))