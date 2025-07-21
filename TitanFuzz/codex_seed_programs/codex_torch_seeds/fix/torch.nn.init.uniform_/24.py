'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.uniform_\ntorch.nn.init.uniform_(tensor, a=0.0, b=1.0)\n'
import torch
from torch.autograd import Variable
import numpy as np
print('\nTask 1: import PyTorch')
print('\nTask 2: Generate input data')
input_data = Variable(torch.randn(5, 3))
print('Input data: \n', input_data)
print('\nTask 3: Call the API torch.nn.init.uniform_')
torch.nn.init.uniform_(input_data, a=0.0, b=1.0)
print('Output data: \n', input_data)
print('\nTask 4: Call the API torch.nn.init.normal_')
torch.nn.init.normal_(input_data, mean=0.0, std=1.0)
print('Output data: \n', input_data)
print('\nTask 5: Call the API torch.nn.init.constant_')