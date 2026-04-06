from .pickers import joined, k, ntimes, pickers, w_picker

stop = 'ɂ'
cons = ['p', 't', 'k', 'm', 'n', 'w', 'pp', 'tt', 'kk', 'mm', 'nn', 'ww']
vowel = ['i', 'e', 'a', 'o']

syll_v = pickers(k(stop), vowel)
syll_cv = pickers(cons, vowel)
syll_cvc = pickers(cons, vowel, cons)

syll_ = w_picker((syll_v, syll_cv, syll_cvc), (20, 40, 10))

w = w_picker([ntimes(syll_, n) for n in (1,2,3,4)], (20, 60, 20, 10))

monosyll = joined(syll_)
disyll = joined(ntimes(syll_, 2))
trisyll = joined(ntimes(syll_, 3))
tetrasyll = joined(ntimes(syll_, 4))

jw = joined(w)
