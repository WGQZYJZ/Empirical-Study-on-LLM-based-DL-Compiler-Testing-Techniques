'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.isneginf\ntorch.isneginf(input, *, out=None)\n'
import torch
import torch
input_data = torch.tensor([(- float('inf')), float('-inf'), float('inf'), float('inf')])
print('Input data: ', input_data)
output = torch.isneginf(input_data)
print('Output: ', output)