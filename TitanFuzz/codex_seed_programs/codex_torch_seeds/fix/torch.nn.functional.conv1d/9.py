'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.conv1d\ntorch.nn.functional.conv1d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1)\n'
import torch
from torch.autograd import Variable
import numpy as np
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.nn.functional.conv1d')
input = Variable(torch.randn(1, 1, 10))
weight = Variable(torch.randn(1, 1, 3))
bias = Variable(torch.randn(1))
print(input)
print(weight)
print(bias)
output = torch.nn.functional.conv1d(input, weight, bias)
print(output)