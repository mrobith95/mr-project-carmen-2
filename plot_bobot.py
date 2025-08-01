import riskfolio as rp
import matplotlib.pyplot as plt

def plot_bobot(w):
    # plot komposisi portfolio
    fig_pie, ax_pie = plt.subplots(figsize=(9,6))
    ax_pie = rp.plot_pie(w=w, title='Asset Composition', others=0.05)
    ax_pie.set_aspect('auto')
    plt.show()