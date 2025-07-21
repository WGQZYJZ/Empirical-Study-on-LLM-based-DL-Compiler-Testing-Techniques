'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RReLU\ntorch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 5, 5))
print('Input data: \n', x)
relu = torch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
y = relu(x)
print('Output data: \n', y)