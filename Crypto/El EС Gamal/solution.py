sage: e = EllipticCurve(GF(3547),[1801,461])
sage: e
Elliptic Curve defined by y^2 = x^3 + 1801*x + 461 over Finite Field of size 3547
sage: P = e(1688,2431)
sage: Q = e(2742,1260)
sage: for k in range(0, len(e.points())):
....:     if Q == k*P:
....:         print (k)
2302
sage: k = 2302
sage: Q == k*P
True
sage:

