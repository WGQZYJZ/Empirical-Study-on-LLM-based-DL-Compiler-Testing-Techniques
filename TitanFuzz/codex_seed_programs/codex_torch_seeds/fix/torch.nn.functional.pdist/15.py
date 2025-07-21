'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pdist\ntorch.nn.functional.pdist(input, p=2)\n'
import torch
import numpy as np
input = torch.rand(5, 3)
output = torch.nn.functional.pdist(input)
print(output)