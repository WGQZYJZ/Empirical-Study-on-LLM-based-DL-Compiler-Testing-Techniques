'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.conv2d\ntorch.nn.functional.conv2d(input, weight, bias=None, stride=1, padding=0, dilation=1, groups=1)\n'
import torch
from torch.autograd import Variable
from torch.nn.functional import conv2d
import torch
from torch.autograd import Variable
from torch.nn.functional import conv2d
input = Variable(torch.randn(1, 1, 4, 4))
weight = Variable(torch.randn(1, 1, 2, 2))
out = conv2d(input, weight)
print(out)
print(out.shape)