import riskfolio as rp
from tabulate import tabulate

def optimize_portfolio(rekam_return):

    ## pertama-tama, definiskan objek portfolio
    port = rp.Portfolio(returns=rekam_return)

    ## kemudian definisikan cara mengestimasi return dan matriks kovarians.
    ## untuk kasus ini, ---
    method_mu = 'hist'
    method_cov = 'hist'
    port.assets_stats(method_mu = method_mu, method_cov=method_cov)

    ## definisikan input lain untuk optimisasi
    model = 'Classic' #model matematika yang dipakai adalah mean-variance biasa
    rm = 'MV' #resiko yang dipertimbangkan. 'MV' menunjukkan variance sebagai resiko
    obj = 'Sharpe' # fungsi objektif. 'Sharpe' menandakan risk-adjusted return
    rf = 0 #risk-free return
    ##

    ## lakukan optimisasi mean-variance
    w = port.optimization(model=model, rm=rm, obj=obj, rf=rf)

    ## buat dataframe baru untuk keperluan display
    dispw = w.copy()
    dispw = 100*dispw
    dispw = (dispw.round(2))

    ## print
    print(tabulate(dispw, headers=['Saham', 'Bobot (%)'],
                tablefmt='outline', floatfmt='.2f'))

    return w, dispw