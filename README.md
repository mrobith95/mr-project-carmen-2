# mr-project-carmen-2
Source code for my Medium Article ["Simple Maximum Sharpe Ratio Portfolio Optimization"](https://medium.com/@mrobith95/simple-maximum-sharpe-ratio-portfolio-optimization-adc45e2697ee). You can use this source code to replicate result on the article or to perform portfolio optimization yourself. It is recommended to use packages listed in `requirements.txt` in order to run this code.

## Disclaimer
This source code, and article linked to this repo, is only for educational and general informational purposes and not a financial/investment advice nor recommendation. You are responsible for your own investment desicions.

## How to Use
If you just want to replicate result in the article, then you only need to run `playground.py` without changes.

If you want to do portfolio optimization by yourself, then modify the following variables on `playground.py` as needed:

* `to_download` : a list of stocks you consider to add for your portfolio. Note that, while you can consider any stocks available from yahoo finance, you can only use IHSG as benchmark index.
* `start_str` : Download start date string (YYYY-MM-DD).
* `end_str` : Download end date string (YYYY-MM-DD).
* `download_path` : Name of folder for which downloaded data would be saved.
* `month_out` : The number of months to set as outsample part period. Must be an integer more than 0.

Note that Download start date is inclusive but Download end date is exclusive. We suggest that ...
1. the number of days of downloaded data at least 10 times the number of considered stocks.
2. the number of months of downloaded data at least 2 times `month_out`.

You must run `download_data` function if it is the time you run `playground.py`. `plot_bobot` function is optional (You may not run this function when performing portfolio optimization). You might need to close several plots that appear to make sure the code run/end perfectly.
