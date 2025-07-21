'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardsigmoid\ntorch.nn.functional.hardsigmoid(input, inplace=False)\n'
import torch
import torch.nn.functional as F
input = torch.randn(2, 3)
print(F.hardsigmoid(input))