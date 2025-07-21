'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.conj_physical\ntorch.conj_physical(input, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 2)
print('Input data:\n', input)
output = torch.conj_physical(input)
print('Output data:\n', output)