import cvxpy as cp
import numpy as np
import pandas as pd
from tabulate import tabulate

def optimize_portfolio(rekam_return):

    nama_saham = rekam_return.columns ## nama-nama saham yang tersedia

    ## pertama, lakukan estimasi vector myu dan matriks kovarians
    myu_vec = rekam_return.mean().to_numpy()
    cov_mat = rekam_return.cov().to_numpy()

    ## definisikan masalah optimisasi
    y = cp.Variable(myu_vec.shape[0]) ## banyak saham terdeteksi pada rekam_return
    rf = np.full_like(myu_vec, 0) ## risk free return. Saat ini asumsikan 0
    vec1 = np.ones_like(myu_vec) ## vektor yang nilainya 1 semua
    ## metode yang digunakan adalah Transformasi Schaible
    fobj = cp.Maximize(y.T @ (myu_vec - rf))
    con1 = y.T @ cov_mat @ y <= 1
    con2 = y >= 0
    prob = cp.Problem(fobj, [con1, con2])
    ## Metode ini menuntut penggunaan Interior-Point sebagai solvernya
    prob.solve() ## selesaikan masalah optimisasi
    print(' ')
    w = y.value / (np.sum(y.value)) ## transformasi balik untuk memperoleh weight

    ## buat numpy baru untuk keperluan display
    dispw = np.round(100*w, decimals=2)

    ## note: luaran w dan dispw masih berupa numpy array, bukan pandas
    ## buat versi 'dataframe' dari w dan dispw
    w_df = pd.DataFrame(w, index=nama_saham, columns=['Weight (%)'])
    dispw_df = pd.DataFrame(dispw, index=nama_saham, columns=['Weight (%)'])

    ## print
    print('--- Bobot/Weight tiap Saham Hasil Optimisasi ---')
    print(tabulate(dispw_df, headers=['Saham', 'Bobot (%)'],
                tablefmt='outline', floatfmt='.2f'))
    print(' ')

    return myu_vec, cov_mat, w_df, dispw_df