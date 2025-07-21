'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.positive\ntorch.positive(input)\n'
import torch
input = torch.randn(2, 3)
print(input)
output = torch.positive(input)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp\ntorch.clamp(input, min, max, out=None)\n'
import torch
input = torch.randn(2, 3)
print(input)
output = torch.clamp(input, min=(- 0.5), max=0.5)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clamp_max\ntorch.clamp_max(input, max, out=None)\n'
import torch
input = torch.randn(2, 3)
print(input)