'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmin\ntorch.nn.Softmin(dim=None)\n'
import torch
import numpy as np
import torch
input = torch.randn(2, 3)
print(input)
output = torch.nn.Softmin(dim=1)(input)
print(output)