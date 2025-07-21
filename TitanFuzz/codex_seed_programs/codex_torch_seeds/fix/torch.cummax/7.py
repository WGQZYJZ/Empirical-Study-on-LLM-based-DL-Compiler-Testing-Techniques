'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummax\ntorch.cummax(input, dim, *, out=None)\n'
import torch
import numpy as np
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print('Input data: \n', input_data)
cummax_data = torch.cummax(input_data, dim=1)
print('Cummax data: \n', cummax_data)