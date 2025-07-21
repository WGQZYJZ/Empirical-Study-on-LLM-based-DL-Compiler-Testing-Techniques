'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sgn\ntorch.sgn(input, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('Task 2: Generate input data')
input_matrix = torch.randn(2, 3)
print('Input Matrix: ', input_matrix)
print('Task 3: Call the API torch.sgn')
output_matrix = torch.sgn(input_matrix)
print('Output Matrix: ', output_matrix)