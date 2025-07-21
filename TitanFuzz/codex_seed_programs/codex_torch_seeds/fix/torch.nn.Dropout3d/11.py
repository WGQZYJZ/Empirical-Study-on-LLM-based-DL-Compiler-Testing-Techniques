'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout3d\ntorch.nn.Dropout3d(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_size = (1, 1, 2, 2, 2)
input_data = Variable(torch.randn(input_size))
dropout = torch.nn.Dropout3d(p=0.5, inplace=False)
output = dropout(input_data)
print('input_data: ', input_data)
print('output: ', output)