'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
input_tensor = torch.randn(4, 4)
print(input_tensor)
clamped_tensor = torch.clamp(input_tensor, min=(- 0.5), max=0.5)
print(clamped_tensor)