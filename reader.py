from scrapper import ScrapperShopee


class Reader:

    hasil = [['Nama Produk','Harga Sebelumnya','Harga','Stok Sebelumnya','Stok',
        'Variasi','Rating','Jumlah Review','Deskripsi','Link Gambar']]

    def first(self,input):

        with open(input) as fp:

            line = fp.readline()
            counter = 1

            while line:

                try:
                    ss = ScrapperShopee(line, counter)
                    hasil_temp = ss.scrappe_first()
                    self.hasil.append(hasil_temp)
                    line = fp.readline()
                    counter += 1
                except Exception as err:
                    print(err)
                    line = fp.readline()
                    counter += 1
            return self.hasil

    def after(self,input,df):

        with open(input) as fp:

            line = fp.readline()
            counter = 1

            while line:

                try:
                    ss = ScrapperShopee(line, counter)
                    hasil_temp = ss.scrappe_next(df,counter)
                    self.hasil.append(hasil_temp)
                    line = fp.readline()
                    counter += 1
                except Exception as err:
                    print(err)
                    line = fp.readline()
                    counter += 1
            return self.hasil