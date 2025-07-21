'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
input_data = torch.randn(20)
print(input_data)
print(torch.clamp(input_data, min=(- 0.5), max=0.5))