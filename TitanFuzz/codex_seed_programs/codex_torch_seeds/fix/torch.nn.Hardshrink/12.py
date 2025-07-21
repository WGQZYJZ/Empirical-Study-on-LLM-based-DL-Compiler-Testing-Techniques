'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 5, 5))
hardshrink = torch.nn.Hardshrink(lambd=0.5)
output = hardshrink(input)
print('input: ', input)
print('output: ', output)