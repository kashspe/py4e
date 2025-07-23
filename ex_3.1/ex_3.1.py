hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)
hm = 40
if h <= 40:
    print(h * r)
elif h > 40:
    hs = h - hm
    rs = r * 1.5
    pay = hm * r + hs * rs
    print(pay)