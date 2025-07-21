'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arccosh\ntorch.arccosh(input, *, out=None)\n'
import torch
input_data = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print('Input data: ', input_data)
output_data = torch.arccosh(input_data)
print('Output data: ', output_data)