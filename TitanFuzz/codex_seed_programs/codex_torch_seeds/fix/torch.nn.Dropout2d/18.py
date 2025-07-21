'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('PyTorch location: ', torch.__file__)
print('\nTask 2: Generate input data')
input_data = torch.randn(1, 1, 4, 4)
print('input_data: \n', input_data)
print('\nTask 3: Call the API torch.nn.Dropout2d')
dropout2d = nn.Dropout2d(p=0.5, inplace=False)
output = dropout2d(input_data)
print('output: \n', output)
print('\nTask 4: Call the API torch.nn.Dropout2d with p=0.0')
dropout2d = nn.Dropout2d(p=0.0, inplace=False)
output = dropout2d(input_data)