'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.transpose\ntorch.transpose(input, dim0, dim1)\n'
import torch
input = torch.randn(2, 3)
print('Input data:\n', input)
transposed_input = torch.transpose(input, 0, 1)
print('Transposed input data:\n', transposed_input)