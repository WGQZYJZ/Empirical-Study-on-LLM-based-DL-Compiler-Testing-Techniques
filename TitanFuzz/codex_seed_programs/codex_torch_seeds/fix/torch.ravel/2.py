'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ravel\ntorch.ravel(input)\n'
import torch
data = torch.ones(2, 3)
print('Input data: ', data)
data_ravel = torch.ravel(data)
print('Output data: ', data_ravel)