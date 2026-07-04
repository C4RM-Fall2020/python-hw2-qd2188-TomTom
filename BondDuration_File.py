import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    totalperiods = m * ppy

    # 总期数 = 年数 * 每年付款次数
    t = np.arange(1, totalperiods + 1)
    time = t / ppy

    # 每一期编号，比如 1,2,3,...,10
    # 每一期的时间，用年来表示
    # 如果 ppy=1，就是 1,2,3,...,10
    # 如果 ppy=2，就是 0.5,1,1.5,...,10
    coupon = face * couponRate / ppy
    cf = np.ones(totalperiods) * coupon
    cf[-1] = cf[-1] + face 

    
    pv = (1 + y / ppy) ** (-t)
    pvcf = cf * pv

    
    bondprice = np.sum(pvcf)

    # duration 的分子 = 每一期时间 * 每一期现值，然后加总
    weightedtime = np.sum(time * pvcf)

    # duration = 加权时间 / 债券价格
    bondduration = weightedtime / bondprice

    
    return(bondduration)
    
    
