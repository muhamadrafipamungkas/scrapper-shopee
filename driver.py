import sys
from scrapper import ScrapperShopee

inp = sys.argv
if(len(inp) == 1):
    print("Harap sertakan link produk Shopee")
else:
    coba = ScrapperShopee(str(inp[1]))
    coba.getPrice()

