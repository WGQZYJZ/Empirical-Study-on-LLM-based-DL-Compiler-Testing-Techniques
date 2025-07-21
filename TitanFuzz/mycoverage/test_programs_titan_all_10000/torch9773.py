import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 10, 10)
output = torch.nn.AdaptiveAvgPool2d(output_size=5)(input)