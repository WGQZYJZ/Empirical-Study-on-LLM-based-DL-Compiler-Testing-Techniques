'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.inv\ntorch.linalg.inv(A, *, out=None)\n'
import torch
A = torch.randn(3, 3)
print('A = \n', A)
A_inv = torch.linalg.inv(A)
print('A_inv = \n', A_inv)
I = torch.matmul(A, A_inv)
print('I = \n', I)