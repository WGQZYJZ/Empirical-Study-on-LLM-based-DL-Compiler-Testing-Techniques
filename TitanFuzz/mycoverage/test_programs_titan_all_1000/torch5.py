import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 10, 10)
avg_pooling = torch.nn.AvgPool2d(kernel_size=3, stride=1, padding=1)
output = avg_pooling(input)