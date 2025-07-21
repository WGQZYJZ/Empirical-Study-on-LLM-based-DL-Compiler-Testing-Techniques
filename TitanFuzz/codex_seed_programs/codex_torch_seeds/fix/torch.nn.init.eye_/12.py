'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.eye_\ntorch.nn.init.eye_(tensor)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randn(2, 3)
print('input_data: {}'.format(input_data))
print('Task 3: Call the API torch.nn.init.eye_')
torch.nn.init.eye_(input_data)
print('input_data: {}'.format(input_data))