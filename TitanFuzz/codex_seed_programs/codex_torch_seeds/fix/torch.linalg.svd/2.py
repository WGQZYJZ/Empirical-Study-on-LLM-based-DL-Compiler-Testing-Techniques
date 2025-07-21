'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.svd\ntorch.linalg.svd(A, full_matrices=True, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('PyTorch location: ', torch.__file__)
print('Task 2: Generate input data')
A = torch.randn(3, 2)
print('A: ', A)
print('Task 3: Call the API torch.linalg.svd')
(U, S, V) = torch.linalg.svd(A)
print('U: ', U)
print('S: ', S)
print('V: ', V)