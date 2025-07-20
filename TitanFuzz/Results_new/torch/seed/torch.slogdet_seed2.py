A = torch.randn(3, 3)
A = A.double()
(sign, logdet) = torch.slogdet(A)
if (sign == 1):
    print('A is positive definite')
elif (sign == (- 1)):
    print('A is negative definite')
else:
    print('A is indefinite')