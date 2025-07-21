'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atanh\ntorch.atanh(input, *, out=None)\n'
import torch
input_data = torch.rand(5, 5)
print('Input data:', input_data)
print('Output data:', torch.atanh(input_data))