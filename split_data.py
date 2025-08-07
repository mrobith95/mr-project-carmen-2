import pandas as pd
from datetime import date

def split_data(rekam_return, out_sample_months):

    ## ubah data date menjadi datetime
    rekam_return['Date'] = rekam_return['Date'].astype('datetime64[ns]')

    ## tentukan bulan dan tahun data outsample
    last_tgl = rekam_return['Date'].max()
    tgr_tgl  = first_date_n_months_prior(last_tgl, out_sample_months-1)
    tgr_tgl = pd.to_datetime(tgr_tgl)

    ## filter data berdasarkan insample + outsample, data asli + data pembanding
    rekam_return_ori = rekam_return.copy()

    rekam_return_insample  = rekam_return[rekam_return['Date']<tgr_tgl].copy() ## insample
    rekam_return_outsample = rekam_return[rekam_return['Date']>=tgr_tgl].copy() ## outsample

    rekam_return_ihsg = rekam_return_insample['^JKSE'].copy()
    rekam_return_ihsg_out = rekam_return_outsample['^JKSE'].copy()

    rekam_return = rekam_return_insample.drop('^JKSE', axis=1)
    rekam_return_out = rekam_return_outsample.drop('^JKSE', axis=1)

    rekam_return_date = rekam_return['Date'].copy()
    rekam_return_date_out = rekam_return_out['Date'].copy()

    rekam_return = rekam_return.drop('Date', axis=1)
    rekam_return_out = rekam_return_out.drop('Date', axis=1)

    return rekam_return_date, rekam_return, rekam_return_ihsg, rekam_return_date_out, rekam_return_out, rekam_return_ihsg_out

## fungsi tambahan untuk mencari tanggal pertama n bulan sebelumnya
def first_date_n_months_prior(given_date, n):
    year = given_date.year
    month = given_date.month - n

    # Adjust year and month if month <= 0
    while month <= 0:
        month += 12
        year -= 1

    return date(year, month, 1)
    