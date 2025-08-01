import pandas as pd

def get_returns(to_download, download_path):
    first_time = True ## penanda looping baru terjadi sekali

    # untuk masing-masing data yang sudah diunduh ...
    for i in range(len(to_download)):

        ## baca data yang terunduh
        stock = to_download[i]
        raw_data = pd.read_csv(download_path+'/'+stock+'.csv')
        data = raw_data.copy() # siapkan copy, agar data asli tidak berubah jika diperlukan

        ## data yang didownload dari yfinance kadang memiliki NaN, terutama di hari libur
        ## 4 baris dibawah ini akan menghilangkan NaN yang ada diakhir data
        kk = max(data.index)
        while pd.isna(data.loc[kk,'Close']):
            data = data.drop(kk)
            kk = kk-1

        if first_time: ## jika loop baru dilakukan pertama kail...

            ## ambil data close
            rekam_close = data[['Date', 'Close']].copy()
            rekam_close.rename({'Close': stock+'_close'}, axis=1, inplace=True)
            first_time = False ## dan ubah flag loop pertama kali jadi False

        else: ## jika loop sudah pernah dilakukan sebelumnya ...

            ## ambil data close, lalu satukan ke data yang sudah ada
            rekam_close_new = data[['Date', 'Close']].copy() ## save rekam_close first
            rekam_close_new.rename({'Close': stock+'_close'}, axis=1, inplace=True)
            rekam_close = rekam_close.merge(rekam_close_new, on='Date', how='outer')

    ## hapus semua NaN yang ada...
    rekam_close = rekam_close.dropna()

    ## sekarang kita siap untuk menghitung return
    rekam_return = rekam_close.copy()

    ## untuk masing-masing data yang diunduh ...
    for i in range(len(to_download)):

        ## hitung return dari data tersebut
        stock = to_download[i]
        rekam_return[stock] = rekam_close[stock+'_close'].pct_change()
        rekam_return.drop(stock+'_close', axis=1, inplace=True)

    rekam_return = rekam_return.dropna() ## hapus semua NaN yang tersisa
    rekam_return_date = rekam_return['Date'].astype('datetime64[ns]') ## simpan data tanggal
    rekam_return = rekam_return.drop('Date', axis=1) # drop data tanggal untuk menyesuaikan input riskfolio-lib

    # pisahkan data IHSG, karena IHSG dipakai sebagai pembanding
    rekam_return_ihsg = rekam_return['^JKSE'].copy()
    rekam_return = rekam_return.drop('^JKSE', axis=1)

    return rekam_return_date, rekam_return, rekam_return_ihsg