import random



def pickers(*seqs):
    def inner():
        out = []
        for s in seqs:
            if callable(s):
                s = s()
            res = random.choice(s)
            if callable(res):
                out.append(res())
            else:
                out.append(res)
        return out
    return inner


def w_picker(seq, weights):
    def inner():
        res = random.choices(seq, weights)[0]
        return res() if callable(res) else res
    return inner




def ntimes(f, times, sep='.'):
    def inner():
        out = []
        for i in range(times):
            out.append(f())
            if sep and i < times - 1:
                out.append(sep)
        return out
    return inner



def joined(f):
    def inner():
        def flt(x):
            if isinstance(x, str):
                return x
            else:
                o = ''
                for v in x:
                    o += flt(v)
            return o
        out = ''
        for el in f():
            out += flt(el)
        return out
    return inner
        

def k(val):
    return lambda: val
