import numpy as np

def getBondPrice(y, face, couponrate, m, ppy=1):
    totalperiods = m * ppy 
    t = np.arange(1,totalperiods + 1)
    coupon = face * couponrate / ppy
    cf = np.ones(totalperiods) * coupon
    cf[-1] = cf[-1] + face
    pv = (1+y / ppy) ** (-t)
    pvcf = pv * cf
    bondprice = np.sum(pvcf)
    return(bondprice)
