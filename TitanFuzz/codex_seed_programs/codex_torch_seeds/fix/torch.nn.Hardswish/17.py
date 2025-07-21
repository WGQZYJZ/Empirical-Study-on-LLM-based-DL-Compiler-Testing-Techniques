'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 3, 3, 3))
hardswish = torch.nn.Hardswish()
output = hardswish(input_data)
print('input_data: ', input_data)
print('output: ', output)