'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmod\ntorch.fmod(input, other, *, out=None)\n'
import torch
import torch
input = torch.randn(4, dtype=torch.float)
other = torch.randn(4, dtype=torch.float)
output = torch.fmod(input, other)
print(output)