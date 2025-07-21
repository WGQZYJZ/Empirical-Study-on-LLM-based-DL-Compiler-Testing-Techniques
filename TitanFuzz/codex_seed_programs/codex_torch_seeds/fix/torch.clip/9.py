'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.clip\ntorch.clip(input, min=None, max=None, *, out=None)\n'
import torch
input = torch.randn(1, 2, 3)
print(input)
min = 0.0
max = 1.0
output = torch.clip(input, min, max)
print(output)