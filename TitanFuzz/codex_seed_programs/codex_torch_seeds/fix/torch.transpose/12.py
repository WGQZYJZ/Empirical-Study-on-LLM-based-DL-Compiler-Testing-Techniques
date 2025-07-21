'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
input_data = torch.randn(3, 4)
print('Input data:')
print(input_data)
transpose_data = torch.transpose(input_data, 0, 1)
print('Transposed data:')
print(transpose_data)