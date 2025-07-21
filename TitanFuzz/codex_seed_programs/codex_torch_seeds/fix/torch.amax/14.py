'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.rand(4, 4)
print('Input data: ', input_data)
print('torch.amax(input_data, dim=0) : ', torch.amax(input_data, dim=0))
print('torch.amax(input_data, dim=1) : ', torch.amax(input_data, dim=1))
print('torch.amax(input_data, dim=1, keepdim=True) : ', torch.amax(input_data, dim=1, keepdim=True))
print('torch.amax(input_data, dim=1, keepdim=False) : ', torch.amax(input_data, dim=1, keepdim=False))