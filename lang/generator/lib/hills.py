from .pickers import joined, ntimes, pickers, w_picker

cons_back_hard = ['G', 'q', 'h']
cons_back_soft = ['r', 'X']
cons_front_hard = ['f', 'd']
cons_front_soft = ['x', 'g']
vowel = ['M', 'N', 'L', 'R']

hard_cons = pickers(cons_back_hard + cons_front_soft)
soft_cons = pickers(cons_back_soft + cons_front_soft)


syll_v = pickers(vowel)
syll_vv = pickers(vowel, vowel)
syll_cv = pickers(hard_cons, vowel)
syll_cvc = pickers(hard_cons, vowel, soft_cons)
syll_cvv = pickers(hard_cons, vowel, vowel)
syll_cvvc = pickers(hard_cons, vowel, vowel, soft_cons)

syll = w_picker(
        (syll_v, syll_vv, syll_cv, syll_cvc, syll_cvv, syll_cvvc),
        (20, 20, 10, 5, 10, 5)
    )


monosyll = joined(syll)
disyll = joined(ntimes(syll, 2))
trisyll = joined(ntimes(syll, 3))
tetrasyll = joined(ntimes(syll, 4))

w = w_picker([ntimes(syll, n) for n in (1,2,3,4)], (20, 40, 15, 5))

jw = joined(w)
