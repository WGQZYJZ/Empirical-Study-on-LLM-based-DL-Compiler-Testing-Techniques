"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
import numpy as np
input = torch.tensor([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
pad = (1, 1, 1, 1)
output = torch.nn.functional.pad(input, pad, mode='constant', value=0)
print(output)