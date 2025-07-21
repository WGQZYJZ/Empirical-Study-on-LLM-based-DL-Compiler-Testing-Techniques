'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.ones(1, 1, 5, 5))
print('input: ', input)
zero_padding = torch.nn.ZeroPad2d(2)
output = zero_padding(input)
print('output: ', output)