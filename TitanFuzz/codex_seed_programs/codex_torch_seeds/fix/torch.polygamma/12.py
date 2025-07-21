'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.polygamma\ntorch.polygamma(n, input, *, out=None)\n'
import torch
print('# Task 1')
print('import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\n# Task 2')
print('Generate input data')
input_data = torch.randn(4, 4)
print('Input data: \n', input_data)
print('\n# Task 3')
print('Call the API torch.polygamma')
output_data = torch.polygamma(5, input_data)
print('Output data: \n', output_data)