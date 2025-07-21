'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RReLU\ntorch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)\n'
import torch
from torch.autograd import Variable
from torch.nn import RReLU
input_data = Variable(torch.randn(1, 3))
rrelu = RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)
output = rrelu(input_data)
print('input data: ', input_data)
print('output: ', output)