import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    totalperiods = m * ppy

    
    t = np.arange(1, totalperiods + 1)
    time = t / ppy

    
    coupon = face * couponRate / ppy
    cf = np.ones(totalperiods) * coupon
    cf[-1] = cf[-1] + face 


    pv = (1 + y / ppy) ** (-t)
    pvcf = cf * pv


    bondprice = np.sum(pvcf)


    weightedtime = np.sum(time * pvcf)

    bondduration = weightedtime / bondprice

return(bondduration)
    
    
