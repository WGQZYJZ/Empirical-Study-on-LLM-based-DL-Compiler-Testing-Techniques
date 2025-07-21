import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, 4)
output = torch.nn.functional.avg_pool2d(input, kernel_size=2, stride=1)