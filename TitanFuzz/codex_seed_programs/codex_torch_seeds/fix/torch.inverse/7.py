'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.inverse\ntorch.inverse(input, *, out=None)\n'
import torch
a = torch.rand(2, 2)
print(a)
print(torch.inverse(a))