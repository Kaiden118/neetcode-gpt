import numpy as np
from typing import Tuple, List


class Solution:
    def batch_norm(self, x: List[List[float]], gamma: List[float], beta: List[float],
                   running_mean: List[float], running_var: List[float],
                   momentum: float, eps: float, training: bool) -> Tuple[List[List[float]], List[float], List[float]]:
        # During training: normalize using batch statistics, then update running stats
        # During inference: normalize using running stats (no batch stats needed)
        # Apply affine transform: y = gamma * x_hat + beta
        # Return (y, running_mean, running_var), all rounded to 4 decimals as lists
        x = np.array(x, dtype=float)
        gamma = np.array(gamma, dtype=float)
        beta = np.array(beta, dtype=float)
        running_mean = np.array(running_mean, dtype=float)
        running_var = np.array(running_var, dtype=float)
        if(training):
            miub = np.mean(x, axis=0)
            sigma = np.mean((x - miub)**2, axis=0)
            x_hat = (x - miub) / np.sqrt(sigma + 1e-5)
            running_mean = (1-momentum) * running_mean + momentum * miub
            running_var = (1-momentum) * running_var + momentum * sigma
        else:
            x_hat = (x - running_mean) / np.sqrt(running_var + 1e-5)

        y = gamma * x_hat + beta
        return (np.round(y, 4).tolist(), np.round(running_mean, 4).tolist(), np.round(running_var, 4).tolist())
        pass
