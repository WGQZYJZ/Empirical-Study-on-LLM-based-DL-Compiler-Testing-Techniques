'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
from torch.autograd import Variable
from torch.nn import Hardswish
input_data = Variable(torch.randn(2, 3))
hardswish = Hardswish()
output = hardswish(input_data)
print('input data: ', input_data)
print('output data: ', output)