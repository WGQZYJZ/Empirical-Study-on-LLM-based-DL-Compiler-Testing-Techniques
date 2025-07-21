'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rsqrt\ntorch.rsqrt(input, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
output = torch.rsqrt(input)
print(output)