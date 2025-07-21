'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RReLU\ntorch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
x = Variable(torch.rand(2, 2))
print('x: \n', x)
relu = nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
y = relu(x)
print('y: \n', y)