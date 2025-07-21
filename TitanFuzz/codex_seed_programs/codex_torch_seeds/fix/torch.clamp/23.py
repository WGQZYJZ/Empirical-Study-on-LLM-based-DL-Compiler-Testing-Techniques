'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min=None, max=None, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input data: \n', input)
torch.clamp(input, min=0.5, max=1.5)
print('Output data: \n', input)