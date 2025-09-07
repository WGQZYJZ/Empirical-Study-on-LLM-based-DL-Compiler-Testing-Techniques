import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, 4)
avg_pool = torch.nn.AdaptiveAvgPool2d(output_size=1)
output = avg_pool(input)