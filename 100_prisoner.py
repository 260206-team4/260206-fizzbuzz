def randomDrawerSampling(x):
    return randomTrialResult(halfOfDrawers)(x)

def kSamplesWithNBoxes(k):
    '''샘플링 횟수와 상자 수에 따른 결과 테이블 구성'''
    tests = range(1, 1 + k)

[optimalDrawerSampling, randomDrawerSampling]

lambda r: '{:.2%}'.format(r)

return lambda n: '\n\n' + fTable(
    str(k) + ' tests of optimal vs random drawer-sampling'
)(fName)(
    lambda r: '{:.2%}'.format(r)
)(
    lambda f: sum(f(n) for x in tests) / k
)([optimalDrawerSampling, randomDrawerSampling])


