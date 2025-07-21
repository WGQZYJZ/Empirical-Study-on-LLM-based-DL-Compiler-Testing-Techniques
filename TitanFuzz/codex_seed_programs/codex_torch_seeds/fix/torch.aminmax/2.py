'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.aminmax\ntorch.aminmax(input, *, dim=None, keepdim=False, out=None)\n'
import torch
import numpy as np
input = torch.rand(4, 4)
print(input)
print(torch.aminmax(input, dim=1))