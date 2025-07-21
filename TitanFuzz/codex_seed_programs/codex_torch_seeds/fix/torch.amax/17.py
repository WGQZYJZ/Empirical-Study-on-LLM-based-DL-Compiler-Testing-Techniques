'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
data = torch.randn(3, 5)
print(data)
print(torch.amax(data, dim=1))