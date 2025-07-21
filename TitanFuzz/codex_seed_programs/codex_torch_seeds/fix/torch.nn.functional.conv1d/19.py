'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.conv1d\ntorch.nn.functional.conv1d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1)\n'
import torch
from torch.autograd import Variable
from torch.nn.functional import conv1d
input_data = Variable(torch.randn(1, 1, 10))
weight = Variable(torch.randn(1, 1, 3))
output = conv1d(input_data, weight)
print(output)