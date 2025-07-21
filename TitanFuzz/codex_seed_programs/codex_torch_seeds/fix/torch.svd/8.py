'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.svd\ntorch.svd(input, some=True, compute_uv=True, *, out=None)\n'
import torch
input = torch.randn(2, 3, 4)
(U, S, V) = torch.svd(input)
print('U =', U)
print('S =', S)
print('V =', V)