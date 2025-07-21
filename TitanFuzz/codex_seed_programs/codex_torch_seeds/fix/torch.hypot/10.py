'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
data1 = torch.randn(1)
data2 = torch.randn(1)
print(data1)
print(data2)
print(torch.hypot(data1, data2))