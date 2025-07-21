'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.log10\ntorch.log10(input, *, out=None)\n'
import torch
data = torch.rand(1)
print('Input:', data)
print('Output:', torch.log10(data))