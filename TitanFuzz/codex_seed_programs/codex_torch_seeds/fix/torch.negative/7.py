'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.negative\ntorch.negative(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
input_data = torch.randn(2, 2)
print('Input data is: ', input_data)
print('Task 3: Call the API torch.negative')
output = torch.negative(input_data)
print('Output is: ', output)