'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.numel\ntorch.numel(input)\n'
import torch
input_data = torch.ones(2, 3)
print('Input data: ', input_data)
print('Number of elements: ', torch.numel(input_data))