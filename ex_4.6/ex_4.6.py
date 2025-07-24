hm = 40
def computepay(h, r):
    return h * r

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h <= 40:
    print("Pay",computepay(h , r))
elif h > 40:
    hs = h - hm
    rs = r * 1.5
    print ("Pay",computepay(hs,rs) + computepay(hm,r))