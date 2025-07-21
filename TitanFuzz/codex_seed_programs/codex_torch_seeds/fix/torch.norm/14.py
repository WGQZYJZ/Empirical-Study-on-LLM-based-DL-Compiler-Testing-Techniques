"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.norm\ntorch.norm(input, p='fro', dim=None, keepdim=False, out=None, dtype=None)\n"
import torch
import numpy as np
input = torch.randn(3, 3)
print(input)
print(torch.norm(input))
print(torch.norm(input, dim=1))
print(torch.norm(input, dim=0))
print(torch.norm(input, dim=1, keepdim=True))
print(torch.norm(input, dim=0, keepdim=True))
print(torch.norm(input, dim=(1, 0)))
print(torch.norm(input, dim=(1, 0), keepdim=True))