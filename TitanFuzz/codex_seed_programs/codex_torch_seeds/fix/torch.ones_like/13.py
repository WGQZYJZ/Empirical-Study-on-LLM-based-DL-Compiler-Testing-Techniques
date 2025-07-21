'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ones_like\ntorch.ones_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
input = torch.randn(2, 3, dtype=torch.float32)
print('Input data:', input)
output = torch.ones_like(input)
print('Output data:', output)