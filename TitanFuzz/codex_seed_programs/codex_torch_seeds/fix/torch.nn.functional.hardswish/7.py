'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardswish\ntorch.nn.functional.hardswish(input, inplace=False)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(2, 3))
print('Input data: ', x)
print('Output data: ', torch.nn.functional.hardswish(x))