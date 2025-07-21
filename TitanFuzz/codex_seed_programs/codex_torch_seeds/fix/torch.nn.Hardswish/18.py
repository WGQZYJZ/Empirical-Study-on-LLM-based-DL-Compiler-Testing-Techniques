'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardswish\ntorch.nn.Hardswish(inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 3, 3))
output = torch.nn.Hardswish(inplace=False)(input)
print('input: ', input)
print('output: ', output)