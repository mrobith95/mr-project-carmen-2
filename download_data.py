import os
import yfinance as yf
import pandas as pd

def download_data(to_download, download_path):

    ## siapkan folder kosong untuk mengunduh data
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    ## download data
    alldata = yf.download(to_download,
                      period='2y', ## untuk menyederhanakan masalah, cukup ambil data 2 tahun sebelumnya
                      rounding = True, ## pembulatan ke 2 angka dibelakang koma
                      auto_adjust = False) ## gunakan OHLC ygn tidak adjust, agar nilainya persis seperti pada chart
    alldata = alldata.reset_index() ## buat tanggal jadi data, bukan index

    # simpan data masing-masing saham dan indeks kedalam csv
    for stock in to_download:
        ini_dict = {}
        ini_dict['Date'] = list(alldata['Date'])
        ini_dict['Open'] = list(alldata[('Open', stock)])
        ini_dict['High'] = list(alldata[('High', stock)])
        ini_dict['Low'] = list(alldata[('Low', stock)])
        ini_dict['Close'] = list(alldata[('Close', stock)])
        ini_dict['Volume'] = list(alldata[('Volume', stock)])

        ini_df = pd.DataFrame.from_dict(ini_dict)

        ini_df.to_csv(download_path+'/'+stock+'.csv')
