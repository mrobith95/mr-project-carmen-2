from download_data import *
from get_returns import *
from optimize_portfolio import *

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
               'TPIA.JK', 'BBNI.JK', 'AMMN.JK', 'GOTO.JK', 'BRPT.JK',
               'AMRT.JK', 'INDF.JK', 'CPIN.JK', 'KLBF.JK', 'ANTM.JK',
               'ADRO.JK', 'BRMS.JK', 'ICBP.JK', 'MDKA.JK', 'PGAS.JK',
               'EXCL.JK', 'INKP.JK', 'UNTR.JK', 'BUMI.JK', 'MBMA.JK',
               'TOWR.JK', 'HEAL.JK', 'PTBA.JK', 'APIC.JK', 'AKRA.JK']

## tentukan semua saham yang ada di salah satu indeks diatas
to_download = list(set(saham_idx30 + sahamidxv30 + sahamidxg30 + sahamidxq30 + saham_eido))
to_download.sort()
to_download.append('^JKSE') ## tambahkan IHSG untuk didownload

## siapkan nama folder tempat mengunduh data
download_path = 'data'

# print(to_download)
# download_data(to_download, download_path) ## download data dari yahoo finance
rekam_return_date, rekam_return, rekam_return_ihsg = get_returns(to_download, download_path) ## dapatkan data return harian
w, dispw = optimize_portfolio(rekam_return)