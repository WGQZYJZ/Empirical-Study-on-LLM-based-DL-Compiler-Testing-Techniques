'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.asin\ntorch.asin(input, *, out=None)\n'
import torch
import math
input = torch.rand(2, 3)
print(input)
output = torch.asin(input)
print(output)