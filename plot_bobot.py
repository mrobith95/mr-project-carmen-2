import matplotlib.pyplot as plt

def plot_bobot(w):
    ## remove 0 weights on w first
    w_ori = w.copy()
    w = w[w>0].dropna().sort_values('Weight (%)')

    ## membuat label kostum
    def label_kustom(idx, val):
        return f'{idx}:{val:1.2f}%'
        
    w['Label'] = [label_kustom(idx, val) for idx, val in zip(w.index, w['Weight (%)'])]

    # plot komposisi portfolio
    fig_pie, ax_pie = plt.subplots(figsize=(9,6))
    ax_pie.pie(w['Weight (%)'].to_numpy().reshape((len(w))), labels = w['Label'],
               radius=1) # wedgeprops dan textprops
    ax_pie.set_title('Weight for each Stock (%)')
    plt.tight_layout()
    plt.show()