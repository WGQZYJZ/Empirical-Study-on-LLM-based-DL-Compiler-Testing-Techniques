'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tril\ntorch.tril(input, diagonal=0, *, out=None)\n'
import torch
import torch
input_data = torch.rand(3, 3)
print('Input data: ', input_data)
output_data = torch.tril(input_data)
print('Output data: ', output_data)