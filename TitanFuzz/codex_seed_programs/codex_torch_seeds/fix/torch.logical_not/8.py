'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.logical_not\ntorch.logical_not(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 0], [1, 1], [0, 1]], dtype=torch.float)
print('input_data: ', input_data)
output = torch.logical_not(input_data)
print('output: ', output)
output = torch.logical_not(input_data, out=input_data)
print('output: ', output)