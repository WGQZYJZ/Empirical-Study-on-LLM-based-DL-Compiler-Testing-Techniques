'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.slogdet\ntorch.linalg.slogdet(A, *, out=None)\n'
import torch
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
A = torch.randn(2, 2)
print('A = ', A)
print('Task 3: Call the API torch.linalg.slogdet')
(sign, logdet) = torch.linalg.slogdet(A)
print('sign = ', sign)
print('logdet = ', logdet)