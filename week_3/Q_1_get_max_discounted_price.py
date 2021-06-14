shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    prices.sort()
    coupons.sort()    

    coupons_index = len(coupons)

    total = 0

    for each in range(coupons_index) :
        max_price = prices.pop()
        max_coupon = coupons.pop()
        total = max_price * ((100 - max_coupon)/100) + total
    
    if prices is not None :
        for each in prices :
            total = total + each

    return total
    



print(get_max_discounted_price(shop_prices, user_coupons))  # 926000 이 나와야 합니다.