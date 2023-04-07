import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2


chat_id = 291445198 # Ваш chat ID, не меняйте название переменной


def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    sum_pow = (x ** 2).sum()
    n = len(x)

    left = np.sqrt(sum_pow / (19 * chi2.ppf(1 - alpha / 2, 2 * n)))
    right = np.sqrt(sum_pow / (19 * chi2.ppf(alpha / 2, 2 * n)))
    
    return (left, right)
