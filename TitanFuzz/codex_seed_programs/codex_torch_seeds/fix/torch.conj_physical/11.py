'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.conj_physical\ntorch.conj_physical(input, *, out=None)\n'
import torch
data = torch.randn(2, 3)
print(data)
print(torch.conj_physical(data))