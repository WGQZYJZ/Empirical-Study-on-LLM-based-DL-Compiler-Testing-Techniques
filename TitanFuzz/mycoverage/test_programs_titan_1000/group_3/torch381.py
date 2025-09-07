import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(1, 1, 4, 4)
pool = torch.nn.AdaptiveMaxPool2d((1, 1))
output = pool(input)
pool = torch.nn.AdaptiveMaxPool2d((2, 2))
output = pool(input)
pool = torch.nn.AdaptiveMaxPool2d((3, 3))
output = pool(input)
pool = torch.nn.AdaptiveMaxPool2d((4, 4))
output = pool(input)