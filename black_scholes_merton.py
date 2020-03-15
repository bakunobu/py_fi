from math import log, sqrt, exp
from scipy import stats


def bsm_call_value(S0, K, T, r, sigma):
    """
    Val of Eur call option in BSM model
    Analitycal formula
    
    Params:
    =======
    S0 : float
        initial stock/index level
    K : float
        strike price
    T : float
        maturity date (in year fractions)
    r : float
        constant risk-free short rate
    sigma : float
        volatility factor in diffusion term
    
    Returns
    =======
    value : float
        percent value of the European call option
    """
    
    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = (log(S0 / K) + (r - 0.5 * sigma ** 2) * T) * (sigma * sqrt(T))
    value = (S0 * stats.norm.cdf(d1, 0.0, 1.0) - K * exp(-r * T) * stats.norm.cdf(d2, 0.0, 1.0))
    return(value)
    # stats.norm.csf = cum distr func for Norm Distr


def bsm_vega(S0, K, T, r, sigma):
     """
    Vega of Eur call option in BSM model

    
    Params:
    =======
    S0 : float
        initial stock/index level
    K : float
        strike price
    T : float
        maturity date (in year fractions)
    r : float
        constant risk-free short rate
    sigma : float
        volatility factor in diffusion term
    
    Returns
    =======
    vega : float
        partial derivative of BSM formula with respect to sigma (i.e. Vega)
    """
    
    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    vega = S0 * stats.norm.cdf(d1, 0.0, 1.0) * sqrt(T)
    return(vega)

def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est, it=100):
    """
    Implied volatility of Eur call option in BSM model

    
    Params:
    =======
    S0 : float
        initial stock/index level
    K : float
        strike price
    T : float
        maturity date (in year fractions)
    r : float
        constant risk-free short rate
    C0 : int ???
        initial quote???
    sigma_est : float
        extimate of imp. volatility
    it : int
        number of iterations
    
    Returns
    =======
    sigma_est : float
        numerically estimated implied volatility
    """

    for i in range(it):
        sigma_est -= ((bsm_call_value(S0, K, T, r, sigma_est) - C0) / bsm_vega(S0, K, T, r, sigma_est))
    return(sigma_est)
    
          
    