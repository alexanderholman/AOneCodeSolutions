## O(n) time and space solution in `python3`

def min_pickup_coupon(coupons):                 
    min_coupon_len = -1
    found = {}
    for i, coupon in enumerate(coupons):
        if coupon in found:
            diff = i - found[coupon] + 1
            if diff < min_coupon_len or min_coupon_len == -1:
                min_coupon_len = diff
            else:
                found[coupon] = i
        else:
            found[coupon] = i
    return min_coupon_len
