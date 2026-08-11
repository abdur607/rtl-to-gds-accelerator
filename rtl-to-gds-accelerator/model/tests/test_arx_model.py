from model.python.arx_model import permute,quarter

def test_deterministic():
    x=0x0123456789abcdeffedcba9876543210
    assert permute(x)==permute(x)

def test_input_sensitivity():
    x=0x0123456789abcdeffedcba9876543210
    assert permute(x)!=permute(x^1)

def test_quarter_words_stay_32bit():
    q=quarter(0xffffffff,0xffffffff,0xffffffff,0xffffffff)
    assert all(0<=x<=0xffffffff for x in q)
