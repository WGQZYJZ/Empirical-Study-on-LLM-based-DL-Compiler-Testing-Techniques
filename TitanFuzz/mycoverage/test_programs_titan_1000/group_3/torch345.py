import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(0, 16).view(1, 1, 16)
pooling = torch.nn.AvgPool1d(kernel_size=3, stride=2, padding=0, ceil_mode=False, count_include_pad=True)
output = pooling(data)