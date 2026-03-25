from .pickers import joined, ntimes, k, pickers, w_picker

vs = ['à', 'á', 'â', 'è', 'é','ê', 'ì', 'í', 'î']

cons = ['t', 'ʈ', 'tʰ', 'c', 'cʰ', 'k', 'kʰ', 'd', 'ɖ', 'ɟ', 'g', 's', 'ʂ', 'ʃ', 'z', 'ʐ']
diphths = ['dz', 'tʃ', 'ʈʂ']
cvc = pickers(
        (pickers(cons, vs, cons),
         pickers(diphths, vs, cons),
         pickers(cons, vs, diphths),
         pickers(diphths, vs, diphths))
        )
cvvc = pickers(
        (pickers(cons, vs, vs, cons),
         pickers(diphths, vs, vs, cons),
         pickers(cons, vs, vs, diphths),
         pickers(diphths, vs, vs, diphths))
        )
cvcc = pickers(
        (pickers(cons, vs, cons, cons),
         pickers(diphths, vs, cons, cons))
        )
cvvcc = pickers(pickers(cons, vs, vs, cons, cons), pickers(diphths, vs, vs, cons, cons))
v = pickers(vs)
vc = pickers(
        (pickers(vs, cons),
         pickers(vs, diphths))
        )
vcc = pickers(vs, cons, cons)
ccv = pickers((pickers(cons, cons, vs), pickers(diphths, vs)))
cvv = pickers((pickers(cons, vs, vs), pickers(diphths, vs, vs)))

syll_ = w_picker((v, vc, vcc, cvc, ccv, cvv, cvvc, cvcc, cvvcc), (20, 30, 10, 30, 30, 30, 20, 10, 10))
monosyll = joined(syll_)
disyll = joined(ntimes(syll_, 2))
trisyll = joined(ntimes(syll_, 3))
tetrasyll = joined(ntimes(syll_, 4))
pentasyll = joined(ntimes(syll_, 5))

w = w_picker([ntimes(syll_, n) for n in (1,2,3,4,5)], (20, 30, 40, 40, 10))

jw = joined(w)
