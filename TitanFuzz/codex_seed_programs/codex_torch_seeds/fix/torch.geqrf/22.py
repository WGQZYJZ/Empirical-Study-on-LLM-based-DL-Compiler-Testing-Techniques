'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.geqrf\ntorch.geqrf(input, *, out=None)\n'
import torch
a = torch.randn(3, 3)
print('Input: \n', a)
(q, r) = torch.geqrf(a)
print('Q: \n', q)
print('R: \n', r)