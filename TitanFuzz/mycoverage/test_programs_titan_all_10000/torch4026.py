import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 5, 5))
pool = torch.nn.AvgPool2d(kernel_size=3, stride=1, padding=0, ceil_mode=False, count_include_pad=True, divisor_override=None)