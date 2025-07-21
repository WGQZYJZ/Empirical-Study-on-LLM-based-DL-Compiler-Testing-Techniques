'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
input_data = np.random.randn(1, 3, 3, 3)
input_data = Variable(torch.Tensor(input_data))
hardswish = torch.nn.Hardswish()
output = hardswish(input_data)
print('input: ', input_data)
print('output: ', output)