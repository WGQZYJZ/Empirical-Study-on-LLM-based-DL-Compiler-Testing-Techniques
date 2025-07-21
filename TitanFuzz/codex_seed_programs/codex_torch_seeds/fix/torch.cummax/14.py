'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cummax\ntorch.cummax(input, dim, *, out=None)\n'
import torch
print('\nTask 1: import PyTorch')
print('\nPyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
input_data = torch.tensor([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
print('\nInput data: ', input_data)
print('\nTask 3: Call the API torch.cummax')
cummax_data = torch.cummax(input_data, dim=0)
print('\nCummax data: ', cummax_data)