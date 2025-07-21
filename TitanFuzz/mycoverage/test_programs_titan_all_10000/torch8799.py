import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 3, 5, 5)
max_pool = torch.nn.AdaptiveMaxPool2d((3, 3))
output = max_pool(input)