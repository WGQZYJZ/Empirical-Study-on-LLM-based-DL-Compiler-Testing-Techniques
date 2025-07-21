'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
print('Input data:')
print(input)
(U, S, V) = torch.svd(input)
print('U:')
print(U)
print('S:')
print(S)
print('V:')
print(V)