'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mv\ntorch.mv(input, vec, *, out=None)\n'
import torch
input = torch.randn(2, 3)
vec = torch.randn(3)
print('input = ', input)
print('vec = ', vec)
output = torch.mv(input, vec)
print('output = ', output)