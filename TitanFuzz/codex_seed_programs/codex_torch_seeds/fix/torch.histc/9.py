'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.histc\ntorch.histc(input, bins=100, min=0, max=0, *, out=None)\n'
import torch
import torch
x = torch.randn(1000)
torch.histc(x, bins=100, min=0, max=0, out=None)
print(torch.histc(x, bins=100, min=0, max=0, out=None))