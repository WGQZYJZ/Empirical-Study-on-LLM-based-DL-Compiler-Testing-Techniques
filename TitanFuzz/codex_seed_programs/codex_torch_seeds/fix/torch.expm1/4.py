'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.expm1\ntorch.expm1(input, *, out=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('Input data: ', input_data)
print('Output data: ', torch.expm1(input_data))