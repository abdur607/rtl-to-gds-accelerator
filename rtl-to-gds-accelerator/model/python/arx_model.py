def u32(x): return x & 0xffffffff
def rol(x,n): return u32((x<<n)|(x>>(32-n)))
def quarter(a,b,c,d):
    a=u32(a+b); d=rol(d^a,16); c=u32(c+d); b=rol(b^c,12)
    a=u32(a+b); d=rol(d^a,8); c=u32(c+d); b=rol(b^c,7)
    return a,b,c,d
def permute(state:int,rounds=12):
    a=state & 0xffffffff; b=(state>>32)&0xffffffff; c=(state>>64)&0xffffffff; d=(state>>96)&0xffffffff
    for _ in range(rounds): a,b,c,d=quarter(a,b,c,d)
    return a | (b<<32) | (c<<64) | (d<<96)
