import numpy as np

def getBondPrice(y, face, couponrate, m, ppy=1):
    # 总期数 = 年数 * 每年付款次数
    # 比如 10 年，每年 2 次，就是 20 期
    totalperiods = m * ppy 

    # 生成每一期的编号
    # 比如 totalperiods = 20，就是 [1,2,3,...,20]
    t = np.arange(1,totalperiods + 1)

    # 每一期的 coupon
    # 年 coupon = face * couponrate
    # 如果一年付 ppy 次，每次 coupon 要除以 ppy
    coupon = face * couponrate / ppy

    # 创建每一期的 cash flow
    # 先默认每一期都是 coupon
    cf = np.ones(totalperiods) * coupon

    # 最后一期除了 coupon，还要还本金 face
    cf[-1] = cf[-1] + face

    # 计算每一期的折现因子
    # Python 里 ** 是次方
    pv = (1+y / ppy) ** (-t)

    # 每一期 cash flow 的现值
    pvcf = pv * cf

    # 债券价格 = 所有现值加总
    bondprice = np.sum(pvcf)
    return(bondprice)
