'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
import numpy as np
input = torch.randn(1, 3)
print(input)
output = torch.rad2deg(input)
print(output)