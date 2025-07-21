'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsin\ntorch.arcsin(input, *, out=None)\n'
import torch
data = torch.randn(1)
print(data)
print(torch.arcsin(data))