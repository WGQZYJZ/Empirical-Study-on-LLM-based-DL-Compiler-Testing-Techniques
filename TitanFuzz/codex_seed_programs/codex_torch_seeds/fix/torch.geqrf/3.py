'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
x = torch.randn(4, 4)
print('Input:')
print(x)
(tau, q) = torch.geqrf(x)
print('Output:')
print('tau:')
print(tau)
print('q:')
print(q)