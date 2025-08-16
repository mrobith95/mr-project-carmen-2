import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mtick
import numpy as np
import pandas as pd
from datetime import timedelta
from tabulate import tabulate
from scipy import stats

def outsample_sim(w, rekam_return_date_out, rekam_return_out, rekam_return_ihsg_out):

    ## combine return data
    apa2 = rekam_return_out @ w
    data = pd.concat([rekam_return_date_out, apa2, rekam_return_ihsg_out], axis=1)
    data = data.rename({'Weight (%)': 'Optimized', '^JKSE':'IHSG'}, axis=1)
    
    ## add 1 date before first outsample
    min_date = data['Date'].min() - timedelta(days=1)
    min_id   = data.index.min() - 1
    data.loc[min_id] = [min_date, 0.0, 0.0]
    data = data.sort_values('Date')

    ## compute cumulative returns and drawdown for both portfolio
    data['Optimized_return'] = (data['Optimized'] + 1).cumprod()
    data['IHSG_return'] = (data['IHSG'] + 1).cumprod()

    data['Optimized_max'] = data['Optimized_return'].cummax()
    data['IHSG_max'] = data['IHSG_return'].cummax()

    data['Optimized_DD'] = data['Optimized_return'] - data['Optimized_max']
    data['IHSG_DD'] = data['IHSG_return'] - data['IHSG_max']

    ## get mean return, standard deviation, sharpe and max DD
    opt_mean = data['Optimized'].mean()
    ihsgmean = data['IHSG'].mean()

    opt_stdev = data['Optimized'].std()
    ihsgstdev = data['IHSG'].std()

    opt_sharpe = opt_mean/opt_stdev
    ihsgsharpe = ihsgmean/ihsgstdev

    opt_maxdd = -1*data['Optimized_DD'].min()
    ihsgmaxdd = -1*data['IHSG_DD'].min()

    opt_med = data['Optimized'].median()
    ihsgmed = data['IHSG'].median()

    opt_iqr = data['Optimized'].quantile(0.75) - data['Optimized'].quantile(0.25)
    ihsgiqr = data['IHSG'].quantile(0.75) - data['IHSG'].quantile(0.25)

    ## buat tabel metrik
    ini_dict = {'Metrik': ['Rata-Rata Return Harian (%)', 'Standar Deviasi Return Harian (%)', 'Median Return Harian (%)', 'IQR Return Harian (%)', 'Sharpe Ratio', 'Max. Drawdown (%)'],
                'Optimized': [round(100*opt_mean,2), round(100*opt_stdev,2), round(100*opt_med,2), round(100*opt_iqr,2), round(opt_sharpe,2), round(100*opt_maxdd,2)],
                'IHSG': [round(100*ihsgmean,2), round(100*ihsgstdev,2), round(100*ihsgmed,2), round(100*ihsgiqr,2), round(ihsgsharpe,2), round(100*ihsgmaxdd,2)],
                'SR022-T5': [0.03, 0.00, 0.03, 0.00, '-', 0.00]}
    
    ini_pd = pd.DataFrame(ini_dict)

    ## print tabel
    print('--- Metrik Portofolio Hasil Optimasi vs. IHSG ---')
    print(tabulate(ini_pd, headers=ini_pd.columns,
                tablefmt='outline', floatfmt='.2f'))
    print(' ')
    
    ## uji KS test untuk membandingkan return portofolio hasil optimisasi dan IHSG
    ## Null: Return hasil optimisasi kurang dari sama dengan return IHSG
    ## Alt : Return hasil optimisasi lebih tinggi dibanding IHSG
    ## threshold = 0.05

    print('--- Uji KS return hasil optimisasi vs. IHSG ---')
    hasil_ks = stats.ks_2samp(data['Optimized'], data['IHSG'],
                              alternative='less')
    print('pvalue hasil KS: ', hasil_ks.pvalue)
    if hasil_ks.pvalue < 0.05:
        print('Kesimpulan: Return hasil optimisasi lebih tinggi dibandingkan IHSG.')
    else:
        print('Kesimpulan: Return hasil optimisasi cenderung tidak lebih tinggi dibandingkan IHSG.')

    ## plot distribusi return
    bin_spec = np.arange(np.floor(min(100*data['Optimized'])),
                        np.ceil(max(100*data['Optimized']))+0.25,
                        0.25)
    bin_spec_ihsg = np.arange(np.floor(min(100*data['IHSG'])),
                        np.ceil(max(100*data['IHSG']))+0.25,
                        0.25)

    fig_hist, ax_hist = plt.subplots(figsize=(9,6))
    ax_hist.hist(100*data['IHSG'], bins=bin_spec_ihsg,
                weights=np.ones_like(data['IHSG'])/len(data['IHSG']),
                edgecolor='black', alpha=0.7, color='#d62728')
    ax_hist.axvline(100*ihsgmean, label=f'Mean (IHSG): {round(100*ihsgmean,2)}%', color='#ff7f0e', lw=2)
    ax_hist.hist(100*data['Optimized'], bins=bin_spec,
                weights=np.ones_like(data['Optimized'])/len(data['Optimized']),
                edgecolor='black', alpha=0.7, color='#2ca02c')
    ax_hist.axvline(100*opt_mean, label=f'Mean (Opt.): {round(100*opt_mean,2)}%', color='#1f77b4', lw=2)
    ax_hist.legend()
    ax_hist.grid(True)
    ax_hist.set_title('Histogram Return Harian')
    ax_hist.set_ylabel('Probability Density')
    ax_hist = plt.tight_layout()
    ax_hist = plt.gca().xaxis.set_major_formatter(mtick.FuncFormatter(lambda x, _: f'{x:.2f}%'))
    ax_hist = plt.gca().xaxis.set_major_locator(mtick.MultipleLocator(1))
    ax_hist = plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))

    ## line plot return kumulatif
    fig_ser_cust, ax_ser_cust = plt.subplots(figsize=(9,6))

    ax_ser_cust.plot(data['Date'], data['IHSG_return'], label='IHSG', color='#d62728')
    ax_ser_cust.plot(data['Date'], data['Optimized_return'], label='Optimized', color='#2ca02c')

    ax_ser_cust.legend()
    ax_ser_cust.grid(True)
    ax_ser_cust.set_title('Return Kumulatif dari Waktu-ke-waktu')
    ax_ser_cust = plt.tight_layout()

    ## drawdown
    fig_dd, ax_dd = plt.subplots(figsize=(9,6))
    ax_dd.plot(data['Date'], data['IHSG_DD'], color='#d62728')
    ax_dd.fill_between(data['Date'], data['IHSG_DD'], 0, color='#d62728', alpha=0.3)
    ax_dd.axhline(-1*ihsgmaxdd, label=f'Max DD (IHSG): {round(100*ihsgmaxdd,2)}%', color='#ff7f0e', lw=2)
    ax_dd.plot(data['Date'], data['Optimized_DD'], color='#2ca02c')
    ax_dd.fill_between(data['Date'], data['Optimized_DD'], 0, color='#2ca02c', alpha=0.3)
    ax_dd.axhline(-1*opt_maxdd, label=f'Max DD (Opt.): {round(100*opt_maxdd,2)}%', color='#1f77b4', lw=2)
    ax_dd.set_ylim(min(data['IHSG_DD'].min(), data['Optimized_DD'].min())*1.1, 0)
    ax_dd.legend()
    ax_dd.grid(True)
    ax_dd.set_title('Drawdown dari Waktu-ke-waktu')
    ax_dd = plt.tight_layout()
    ax_dd = plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(xmax=1.0))

    plt.show()

    return ini_pd