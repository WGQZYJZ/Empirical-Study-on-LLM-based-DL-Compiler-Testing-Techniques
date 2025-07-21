'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.slogdet\ntorch.slogdet(input)\n'
import torch
A = torch.randn(3, 3)
A = A.double()
print(A)
(sign, logdet) = torch.slogdet(A)
print(sign)
print(logdet)
if (sign == 1):
    print('A is positive definite')
elif (sign == (- 1)):
    print('A is negative definite')
else:
    print('A is indefinite')