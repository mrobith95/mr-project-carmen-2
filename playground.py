from download_data import *
from get_returns import *
from optimize_portfolio import *
from plot_bobot import *
from split_data import *
from outsample_sim import *

## NOTE: jika Anda berencana untuk mereplikasi hasil yang ada pada artikel
## "Optimasi Portofolio Sederhana pada Pasar Saham Indonesia"
## maka anda dapat run file ini saja, tanpa harus mengubah variabel lainnya.
##
## Jika Anda ingin melakukan optimasi portofolio secara mandiri, ubah variabel berikut:
## to_download  : berisi saham apa saja yang ingin dipertimbangkan untuk masuk dalam portofolio.
##                meskipun Anda bisa menggunakan data saham apa saja yang tersedia di yahoo finance,
##                perhatikan bahwa Anda hanya bisa membandingkannya dengan IHSG.
## start_str    : tanggal awal dari data yang akan didownload
## end_str      : tanggal akhir dari data yang akan didownload
##                perhatikan bahwa data yang didownload mulai dari tanggal pada start_str hingga 1 hari sebelum end_str.
##                untuk menentukan periode data yang diunduh, disarankan agar ...
##                1. banyak harinya minimal 10 * (banyak saham yang dipertimbangkan)
##                2. banyak bulannya minimal 2 kali dari input month_out 
## download_path: nama folder tempat menyimpan data yang didownload
## month_out    : banyak bulan untuk dijadikan data outsample.
##                harus bilangan bulat (integer) lebih dari 0
## Anda wajib menjalankan fungsi download_data jika baru pertama kali menjalankan program ini
## fungsi plot_bobot bersifat fungsional.
## Anda mungkin perlu meg-close beberapa plot yang muncul agar program berjalan/berhenti dengan sempurna.


## list semua saham yang terindeks di masing-masing indeks/ETF
saham_idx30 = ['ADRO.JK', 'AKRA.JK', 'AMRT.JK', 'ANTM.JK', 'ASII.JK', ## Perhatikan untuk saham indonesia punya akhiran '.JK' di entrinya
               'BBCA.JK', 'BBNI.JK', 'BBRI.JK', 'BBTN.JK', 'BMRI.JK',
               'BRPT.JK', 'CPIN.JK', 'EXCL.JK', 'GOTO.JK', 'ICBP.JK',
               'INCO.JK', 'INDF.JK', 'INKP.JK', 'ISAT.JK', 'KLBF.JK',
               'MAPI.JK', 'MBMA.JK', 'MDKA.JK', 'MEDC.JK', 'PGAS.JK',
               'PTBA.JK', 'SMGR.JK', 'TLKM.JK', 'UNTR.JK', 'UNVR.JK']

sahamidxv30 = ['ADRO.JK', 'ASII.JK', 'AUTO.JK', 'BBTN.JK', 'BMTR.JK',
               'BNGA.JK', 'BSDE.JK', 'CTRA.JK', 'ELSA.JK', 'ENRG.JK',
               'ERAA.JK', 'GGRM.JK', 'GJTL.JK', 'HRUM.JK', 'INDF.JK',
               'INDY.JK', 'INKP.JK', 'ITMG.JK', 'JSMR.JK', 'LSIP.JK',
               'MEDC.JK', 'MNCN.JK', 'NISP.JK', 'PGAS.JK', 'PNLF.JK',
               'SMGR.JK', 'SMRA.JK', 'SRTG.JK', 'TKIM.JK', 'UNTR.JK']

sahamidxg30 = ['AKRA.JK', 'AMRT.JK', 'AUTO.JK', 'BBCA.JK', 'BBNI.JK',
               'BBRI.JK', 'BMRI.JK', 'BMTR.JK', 'BNGA.JK', 'BRIS.JK',
               'CTRA.JK', 'ENRG.JK', 'ESSA.JK', 'HEAL.JK', 'ICBP.JK',
               'INDF.JK', 'INDY.JK', 'INKP.JK', 'ISAT.JK', 'ITMG.JK',
               'JPFA.JK', 'KLBF.JK', 'LSIP.JK', 'MAPA.JK', 'MIDI.JK',
               'MIKA.JK', 'NISP.JK', 'SSIA.JK', 'TKIM.JK', 'TLKM.JK']

sahamidxq30 = ['ACES.JK', 'ADMR.JK', 'ADRO.JK', 'AKRA.JK', 'AMRT.JK',
               'ASII.JK', 'AVIA.JK', 'BBCA.JK', 'BBRI.JK', 'BFIN.JK',
               'BMRI.JK', 'BNGA.JK', 'BRIS.JK', 'BTPS.JK', 'CMRY.JK',
               'CPIN.JK', 'INCO.JK', 'INTP.JK', 'KLBF.JK', 'LSIP.JK',
               'MIKA.JK', 'MNCN.JK', 'MYOR.JK', 'NISP.JK', 'PTBA.JK',
               'SCMA.JK', 'SIDO.JK', 'TAPG.JK', 'TLKM.JK', 'UNTR.JK']

saham_eido  = ['BBCA.JK', 'BBRI.JK', 'BMRI.JK', 'TLKM.JK', 'ASII.JK',
               'BBNI.JK', 'GOTO.JK', 'AMMN.JK', 'TPIA.JK', 'AMRT.JK',
               'CPIN.JK', 'INDF.JK', 'ADRO.JK', 'KLBF.JK', 'ICBP.JK',
               'BRPT.JK', 'BRMS.JK', 'UNTR.JK', 'PGAS.JK', 'INKP.JK',
               'MDKA.JK', 'UNVR.JK', 'ANTM.JK', 'MAPI.JK', 'BUMI.JK',
               'PTBA.JK', 'TOWR.JK', 'JPFA.JK', 'ITMG.JK', 'SMGR.JK']

## tentukan semua saham yang ada di salah satu indeks diatas
to_download = list(set(saham_idx30 + sahamidxv30 + sahamidxg30 + sahamidxq30 + saham_eido))
to_download.sort()
to_download.append('^JKSE') ## tambahkan IHSG untuk didownload

## pilih tanggal awal dan akhir dari data yang akan diunduh
start_str = '2022-04-01'
end_str   = '2025-08-01' ## Note: tanggal akhir excluded (tidak ikut diunduh) jika menggunakan yfinance

## siapkan nama folder tempat mengunduh data
download_path = 'data'

month_out = 3 ## banyak bulan untuk data outsample

download_data(to_download, download_path, start_str, end_str) ## download data dari yahoo finance (wajib dilakukan jika baru pertama kali)
rekam_return = get_returns(to_download, download_path) ## dapatkan data return harian
rekam_return_date, rekam_return, rekam_return_ihsg, rekam_return_date_out, rekam_return_out, rekam_return_ihsg_out = split_data(rekam_return, month_out) ## pisahkan data outsample dan pembanding
## data insample akan dipakai untuk optimisasi
## data outsample dipakai untuk melihat performa
myu_vec, cov_mat, w, dispw = optimize_portfolio(rekam_return) ## dapatkan weighting / bobot optimal
plot_bobot(dispw) ## plot bobot masing-masing saham pada portfolio (opsional)
apa = outsample_sim(w, rekam_return_date_out, rekam_return_out, rekam_return_ihsg_out) ## menguji hasil optimisasi pada data outsample
