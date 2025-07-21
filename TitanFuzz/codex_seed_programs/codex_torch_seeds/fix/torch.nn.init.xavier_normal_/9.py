'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
from torch.autograd import Variable
print('\nTask 1: import PyTorch')
print('PyTorch version: ', torch.__version__)
print('\nTask 2: Generate input data')
input_data = torch.randn(1, 3)
print('Input data: ', input_data)
print('\nTask 3: Call the API torch.nn.init.xavier_normal_')
print('torch.nn.init.xavier_normal_(tensor, gain=1.0)')
torch.nn.init.xavier_normal_(input_data, gain=1.0)
print('Output data: ', input_data)