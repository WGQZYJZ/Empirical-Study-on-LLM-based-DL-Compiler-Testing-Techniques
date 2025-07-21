'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.mode\ntorch.mode(input, dim=-1, keepdim=False, *, out=None)\n'
import torch
in_data = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print('Input data:\n', in_data)
print('\nMode of the input data:\n', torch.mode(in_data))
print('\nMode of the input data along the rows:\n', torch.mode(in_data, dim=1))
print('\nMode of the input data along the columns:\n', torch.mode(in_data, dim=0))