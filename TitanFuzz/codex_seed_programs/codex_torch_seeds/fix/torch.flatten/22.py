'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flatten\ntorch.flatten(input, start_dim=0, end_dim=-1)\n'
import torch
import numpy as np
input = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8]])
print('Input: ', input)
output = torch.flatten(input)
print('Output: ', output)