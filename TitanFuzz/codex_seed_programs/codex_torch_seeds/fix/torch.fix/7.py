'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fix\ntorch.fix(input, *, out=None)\n'
import torch
import torch
input = torch.randn(2, 3)
print(input)
output = torch.fix(input)
print(output)