'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.abs\ntorch.abs(input, *, out=None)\n'
import torch
input = torch.randn(1, 1)
print(input)
abs_output = torch.abs(input)
print(abs_output)