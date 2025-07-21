'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
data = torch.randn(1, 10)
print(data)
torch.cos(data, out=None)