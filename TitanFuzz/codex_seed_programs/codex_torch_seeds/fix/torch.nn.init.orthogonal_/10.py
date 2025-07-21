'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.orthogonal_\ntorch.nn.init.orthogonal_(tensor, gain=1)\n'
import torch
import numpy as np
input_size = (1, 3, 5, 5)
input_data = torch.randn(input_size)
print('Input data: ', input_data)
torch.nn.init.orthogonal_(input_data)
print('After orthogonal_: ', input_data)
input_size = (1, 3, 5, 5)
input_data = torch.randn(input_size)
print('Input data: ', input_data)
torch.nn.init.orthogonal_(input_data, gain=2)
print('After orthogonal_: ', input_data)