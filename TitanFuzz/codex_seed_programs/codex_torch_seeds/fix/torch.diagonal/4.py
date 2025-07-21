'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.diagonal\ntorch.diagonal(input, offset=0, dim1=0, dim2=1)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data is: \n', input_data)
diagonal_data = torch.diagonal(input_data)
print('Diagonal data is: \n', diagonal_data)
diagonal_data = torch.diagonal(input_data, offset=1)
print('Diagonal data is: \n', diagonal_data)
diagonal_data = torch.diagonal(input_data, offset=(- 1))
print('Diagonal data is: \n', diagonal_data)
diagonal_data = torch.diagonal(input_data, dim1=1, dim2=0)
print('Diagonal data is: \n', diagonal_data)
diagonal_data = torch.diagonal(input_data, dim1=0, dim2=1)
print('Diagonal data is: \n', diagonal_data)