import os
import errno
import time
import pandas as pd
from reader import Reader

input = 'link.txt'
output = r'data_produk.xls'


def open_file():

    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY

    try:

        os.open(output, flags)

    except OSError as e:

        if e.errno == errno.EEXIST:  # Failed as the file already exists.
            df = pd.read_excel(output, skip_rows=0)
            baca = Reader()
            hasil = baca.after(input,df)
            df = pd.DataFrame(hasil)
            df.to_excel(output, header = False)

        else:  # Something unexpected went wrong so reraise the exception.
            raise Exception("Gagal membuka file {}".format(output))

    else:  # No exception, so the file must have been created successfully.
        baca = Reader()
        hasil = baca.first(input)
        df = pd.DataFrame(hasil)
        df.to_excel(output, header = False)


if __name__ == "__main__":
    
    open_file()
    