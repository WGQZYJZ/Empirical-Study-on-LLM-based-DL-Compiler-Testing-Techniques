'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log2\ntorch.log2(input, *, out=None)\n'
import torch
data = torch.randn(10, 10)
print(data)
print(torch.log2(data))