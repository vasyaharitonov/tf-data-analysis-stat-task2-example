import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 291445198 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    loc = x.mean()
    n = len(x)
    df = n - 1
    scale = np.sqrt(np.var(x))
    
    displ_coeff = 2.33

    return np.sqrt((n-1) * scale*scale / chi2.ppf(1 - alpha/2, df) / 19 * displ_coeff), \
           np.sqrt((n-1) * scale*scale / chi2.ppf(alpha/2, df) / 19 * displ_coeff)
