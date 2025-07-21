'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.flipud\ntorch.flipud(input)\n'
import torch
input_data = torch.arange(1, 11)
print('Input data: ', input_data)
print('Output data: ', torch.flipud(input_data))