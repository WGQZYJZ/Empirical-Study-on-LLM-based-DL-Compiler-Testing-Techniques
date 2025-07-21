import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16, 50, 32)
maxpool = torch.nn.MaxPool2d(kernel_size=2, stride=2)
output = maxpool(input)