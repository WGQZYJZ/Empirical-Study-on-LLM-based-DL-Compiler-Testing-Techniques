'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
tensor_x = torch.randn(2, 3)
print('tensor_x:', tensor_x)
tensor_clamp = torch.clamp(tensor_x, min=(- 0.5), max=0.5)
print('tensor_clamp:', tensor_clamp)