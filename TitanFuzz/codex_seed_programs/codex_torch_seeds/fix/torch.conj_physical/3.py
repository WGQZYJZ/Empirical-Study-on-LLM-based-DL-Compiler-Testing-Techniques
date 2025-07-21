'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.conj_physical\ntorch.conj_physical(input, *, out=None)\n'
import torch
input = torch.randn(2, 3, 5)
print(input)
print(torch.conj_physical(input))